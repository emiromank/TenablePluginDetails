# PluginDetailsTenable
simple py script to extract Tenable Plugins data, via GET request. (Without API key)

## how to:
python3 scriptCLI.py <FILENAME>

![image](https://github.com/emiromank/PluginDetailsTenable/assets/76065274/ca4cecf0-be65-476c-aeb6-544064891c04)

File should have an ID in each line

![image](https://github.com/emiromank/PluginDetailsTenable/assets/76065274/9ed4fa45-bfdb-4cd4-bf83-6dc535c71f70)


## output:
CSV with Plugin ID, Plugin Name, Severity, CVSSv3, v3 Vector

![image](https://github.com/emiromank/PluginDetailsTenable/assets/76065274/f7f30cae-50fe-4ff0-a868-2605a7194237)

## known errors:
Deprecated plugins won't show severity on CSV


