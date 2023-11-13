# probesight by lowkey


## Overview

This tool, created by lowkey, is designed for various subdomain scanning tasks. It provides several commands to perform specific actions related to subdomains, including fingerprinting, port scanning, probing for alive servers, requesting page data, taking screenshots, and finding open-source URLs.

## Installation

Clone the repository:

```bash
git clone https://github.com/lowkeycrack/your-repo.git
cd your-repo

Install dependencies:

bash

pip install -r requirements.txt

Install additional tools (requires sudo):

bash

sudo python install.py

Install additional modules:

bash

python setup.py install

Usage
Fingerprint Command

Fingerprint a list of subdomains.
Usage

bash

python main.py fingerprint [OPTIONS]

Options

    -fn, --filename TEXT: Specify the filename containing a list of subdomains.
    -o, --output TEXT: Specify the output file for the results.
    -d, --domain TEXT: Specify the name of the subdomain in the format: -d subdomain.example.com.
    -ag, --aggression INTEGER: Set the level of aggression for the fingerprinting (e.g., '-ag 1'). Options: 1 (stealthy), 2 (aggressive), 3 (heavy). Default is 1.
    --help: Show the help message and exit.

Example

Fingerprint subdomains from a file and save the results:

bash

python main.py fingerprint -fn subdomain_list.txt -o output.txt
Run Command

Run all the scans and put every single subdomain in a single directory.
Usage

bash

python main.py run [OPTIONS]

Options

    -fn, --filename TEXT: Specify the name of the file containing subdomains.
    -st, --scantype TEXT: Specify the scan type to be used in Nmap. Default is '-sT' (stealth scan).
    -m, --method TEXT: Specify the method to be used. Default is 'GET'.
    -ag, --aggression INTEGER: Set the level of aggression for the scans (e.g., '-ag 1'). Options: 1 (stealthy), 2 (aggressive), 3 (heavy). Default is 1.
    --help: Show the help message and exit.

Example

Run all scans and organize subdomains in a single directory:

bash

python main.py run -fn subdomain_list.txt -st '-sT' -m GET -ag 1


Contributing

If you would like to collaborate or contribute to the development of this tool, feel free to DM on Instagram @kriis._.x05.
License

This project is licensed under the MIT License.
