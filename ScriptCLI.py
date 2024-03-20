import requests
import re
import csv
import sys

csv_file_path = "./output.csv"
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Plugin ID","Plugin Name", "Severity", "CVSSv3", "v3 Vector"]) 

    filename = sys.argv[1]

    with open(filename, "r") as file:
        plugin_ids = file.read().splitlines()

    for plugin_id in plugin_ids:
        url = f"https://www.tenable.com/plugins/nessus/{plugin_id}"
        response = requests.get(url)
        print("working on plugin id: ", plugin_id)
        if response.status_code == 200:
                file_contents = response.text
                # Extract the value from "public_display"
                public_display = file_contents.split('"public_display":"')[1].split('"')[0]

                script_name = file_contents.split('"script_name":"')[1].split('"')[0]
                # Extract the value from "<span class="badge badge-info">
                badge = re.findall(r'<span class="badge (.*?)">', file_contents)

                # Check if badge is not empty and if it is equal to "badge-info"
                if badge and badge[0] == "badge-info":
                    badge = "Info"
                elif badge and badge[0] == "badge-medium":
                    badge = "Medium"
                elif badge and badge[0] == "badge-low":
                    badge = "Low"
                elif badge and badge[0] == "badge-high":
                    badge = "High"
                elif badge and badge[0] == "badge-critical":
                    badge = "Critical"

                if badge == "Info":
                    cvss = "N/A"
                    vector = "N/A"
                else:
                    cvss = file_contents.split('"cvss3_base_score":"')[1].split('"')[0] if '"cvss3_base_score":"' in file_contents else "N/A"
                    vector = file_contents.split('"cvss3_vector":"')[1].split('"')[0] if '"cvss3_vector":"' in file_contents else "N/A"

                # Write CSV file
                writer.writerow([public_display,script_name, badge, cvss, vector])

        else:
            # Handle the error
            print(f"Error accessing URL: {url}")


    print("done.")
