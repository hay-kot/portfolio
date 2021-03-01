---
title: SSH Login Notifications in Home Assistant With Node-Red
path: /ssh-notifications-in-home-assistant
date: 2021-01-05T06:13:31.000+00:00
summary: Adding SSH logging to Home Assistant is super easy to do and can offer a tiny sliver of reassurance that your whole system isn't burning down by an unauthorized user.
reading_time: 
tags: ['frontend', 'coding', 'vue']
image: https://blog.hay-kot.dev/content/images/2021/01/home_assistant_ssh.png
---

[Home Assistant](https://www.home-assistant.io/) is best described by the project themselves


> Open source home automation that puts local control and privacy first. Powered by a worldwide community of tinkerers and DIY enthusiasts. Perfect to run on a Raspberry Pi or a local server.

As an avid self-hosting and chronic time waster, Hoem Assistant is a gold mine of little projects here an there that balloon into a massive and critical part of my home. I dread the day the batteries run out on my motion sensors and I have to **manually** turn the lights on. As such a critical part of my home infrastructure, I've come to have a thought nearly anytime I do a project. How does this integrate into Home Assistant?  

For Christmas my lovely wife was nice enough to get me a subscription to a VPS so I could host a blog and run a few other things in the cloud. As the paranoid self-hoster I am, I wanted to get notifications for SSH Logins and loop those into Home Assistant for extra convenience. Solving this problem was WAY easier than I imagined. With a short script and a little data formatting, I was able to create a [Logbook Card](https://www.home-assistant.io/lovelace/logbook/) on my dashboard that showed recent activity. 

In Home Assistant - Node-Red
----------------------------

We'll be using a webhook to receive data from the server on Home Assistant. To do this, there are two options. Using Node-Red, or using yaml. A long time ago I decided to shift all my automation from yaml to Node-Red so that is the path I recommend and will go over here. However you can accomplish the same using yaml with a combination of webhooks and Data Templating.

 With Node-Red you'll need to create a webhook node and generate a random URL (save this for later). Connect that to a JSON block to process the posted data into a JavaScript object and optionally pass that through a Change Node to set the Topic, and a Delay Node to limit the messages. Finally you need to map the actually value to an Entity Node. We'll be using the payload.message object to hold the entity sensor value. 

![](https://blog.hay-kot.dev/content/images/2021/01/flow-Example-1.png)Flow Example![](https://blog.hay-kot.dev/content/images/2021/01/ssh_entity_node_config.png)
```
Entity Payload[{"id":"ac17221d.ca7b4","type":"ha-webhook","z":"bee214af.688e28","name":"SSH Notification Webhook","server":"15e97f32.f16891","outputs":1,"webhookId":"MY-SSH-WEBHOOK","payloadLocation":"payload","payloadLocationType":"msg","headersLocation":"","headersLocationType":"none","x":130,"y":400,"wires":[["6812e653.224d68"]]},{"id":"38588fad.38fd88","type":"ha-entity","z":"bee214af.688e28","name":"SSH Entity","server":"15e97f32.f16891","version":1,"debugenabled":false,"outputs":1,"entityType":"sensor","config":[{"property":"name","value":"SSH Login"},{"property":"device\_class","value":""},{"property":"icon","value":""},{"property":"unit\_of\_measurement","value":""}],"state":"payload.message","stateType":"msg","attributes":[],"resend":true,"outputLocation":"","outputLocationType":"none","inputOverride":"allow","x":750,"y":400,"wires":[[]]},{"id":"78b836a5.441e78","type":"delay","z":"bee214af.688e28","name":"","pauseType":"rate","timeout":"5","timeoutUnits":"seconds","rate":"1","nbRateUnits":"1","rateUnits":"minute","randomFirst":"1","randomLast":"5","randomUnits":"seconds","drop":true,"x":530,"y":400,"wires":[["38588fad.38fd88"]]},{"id":"6812e653.224d68","type":"json","z":"bee214af.688e28","name":"","property":"payload","action":"obj","pretty":false,"x":290,"y":400,"wires":[["78b836a5.441e78","b22a904e.f459"]]},{"id":"b22a904e.f459","type":"change","z":"bee214af.688e28","name":"Set Topic","rules":[{"t":"move","p":"payload.topic","pt":"msg","to":"topic","tot":"msg"}],"action":"","property":"","from":"","to":"","reg":false,"x":400,"y":400,"wires":[["78b836a5.441e78"]]},{"id":"15e97f32.f16891","type":"server","name":"Home Assistant"}]Code SampleOn The Server
```

On the server you'd like to recieve notifications for you need to create/edit /etc/ssh/sshrc This file can be used to execute scripts on ssh login and is a built in functionality. Open in sshrc and paste in a version of the code below, while replacing the relevent information and formatting the message how you prefer. 
```bash
#!/bin/bash

ip=$(echo "$SSH\_CONNECTION" | cut -d " " -f 1)
hs=$(hostname)

hostIP="$(ip address show dev eth0 | grep "inet " | head --lines=1 | cut --delimiter=' ' --fields=6 | cut --delimiter='/' --fields=1)"

logger -t ssh-wrapper "$USER" login from "$ip"

curl --header "Content-Type: application/json" \
 --request POST \
 --data \
 '{"topic": "'"$hs"'",
 "host": "'"$hs"'",
 "hostIP": "'"$hostIP"'",
 "user": "'"$USER"'",
 "from": "'"$ip"'",
 "message": "'"$USER@$hs just logged in from $ip"'"}' \
 https://homeassistant.mydomain.com/api/webhook/UNIQUE\_KEY
```

Script updated 1/6/21, changes courtesy of @JonTheNiceGuyI've added some some additional key/value pairs to show how to extend that data you might get from the server. These can all be accessed as a JavaScript object in Node-Red

WARNING: If you use Ansible to work on the server, after doing this and running an Ansible script, you may experience a bombardment of notifications. 

Setting up the Card
-------------------

Thanks to the Logbook Card, setup is easy and can be done from the UI. Edit the Lovelace dashboard you'd like to add the card to. Select Add Card and choose the Logbook Card. There you can select the sensor you created in the previous step, how many hours to show, and some other configuration information. 

type: logbook
entities:
 - sensor.ssh\_login
hours\_to\_show: 24
![](https://blog.hay-kot.dev/content/images/2021/01/ssh_log-1.png)Adding SSH logging to Home Assistant is super easy to do and can offer a tiny sliver of reassurance that your whole system isn't burning down by an unauthorized user.

