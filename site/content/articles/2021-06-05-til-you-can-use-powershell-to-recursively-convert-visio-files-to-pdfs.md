---
title: TIL Converting Visio to PDFs Recursively
path: /til-you-can-use-powershell-to-recursively-convert-visio-files-to-pdfs
date: 2021-06-05
summary: Today I learned that you can use powershell on windows to recursively convert visio files to PDF files.
reading_time: 1 Minute Read
tags: ['TIL', 'automation', 'powershell', 'windows']
image: /til-you-can-use-powershell-to-recursively-convert-visio-files-to-pdfs/powershell-logo.png
---




Today I learned that you can use powershell on windows to recursively convert visio files to PDF files. I've found that when working with design drawings that packaging up a directory of visio files into PDFs is time consuming as most converters don't support Visio formats. Powershell on the other hand can interface directly with the Visio ComObject and do the conversion natively on windows. 

```powershell
$drawings = Get-ChildItem -Recurse -Filter "*.vsdx" # Remove Recurse if you don't want to go into nested directories
$drawings += Get-ChildItem -Recurse -Filter "*.vsd"
Write-Host "Converting Visio documents to PDF..." -ForegroundColor Cyan

try
{
    $visio = New-Object -ComObject Visio.Application
    $visio.Visible = $true # If you want to disable the Visio window you can set this to $false


    $i = 0
    foreach ($drawing in $drawings)
    {
        $pdfname = [IO.Path]::ChangeExtension($drawing.FullName, '.pdf')
        Write-Host "Converting:" $drawing.FullName "to" $pdfname
        $document = $visio.Documents.Open($drawing.FullName)
        # Export all pages to PDF, see constants here http://msdn.microsoft.com/en-us/library/office/ff766893.aspx
        $document.ExportAsFixedFormat(1, $pdfname, 1, 0)
        $document.Saved = $true
        $document.Close()
    }

}

catch
{
    Write-Error $_
}

finally
{
    if ($visio) 
    {
        $visio.Quit()
    }

}

```