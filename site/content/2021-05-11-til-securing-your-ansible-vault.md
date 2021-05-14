---
title: TIL Securing Your Ansible Vault
path: /til-securing-your-ansible-vault
date: 2021-05-11 21:16:28.812566
summary: Today I learned you can setup a pre-commit hook to keep you from committing your secrets to source control.
reading_time: 1 Minute Read
tags: ['TIL', 'Ansible', 'Homelab']
image: /til-securing-your-ansible-vault/ansible-logo.png
---

Credit for this little trick goes to Ironic Badger's Ansible [github repository](https://github.com/IronicBadger/infra/blob/master/git-init.sh). Which he has stolen from someone else! 

When setting up your Ansible playbooks you can include this script in the top directory and run it from the terminal to add this pre-commit hook. This will check to see if your vault is encrypted before committing to source control. Make sure you set the correct path for your vault!

```bash
#!/bin/bash
# sets up a pre-commit hook to ensure that vault.yaml is encrypted
#
# credit goes to nick busey from homelabos for this neat little trick
# https://gitlab.com/NickBusey/HomelabOS/-/issues/355

if [ -d .git/ ]; then
rm .git/hooks/pre-commit
cat <<EOT >> .git/hooks/pre-commit
if ( git show :vars/vault.yaml | grep -q "\$ANSIBLE_VAULT;" ); then
echo "[38;5;108mVault Encrypted. Safe to commit.[0m"
else
echo "[38;5;208mVault not encrypted! Run 'make encrypt' and try again.[0m"
exit 1
fi
EOT

fi

chmod +x .git/hooks/pre-commit
```

## Additional Tip

Use a makefile for easily running your Ansible playbook from the command line without trying in your password. Use the entry below and create a file with your vault password in `.value-password`.

```makefile
remote:
	ansible-playbook ansible/playbook.remote.yml --vault-password-file .vault-password

```