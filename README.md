# WDoS
Wireless Deauth program in  python2 


https://github.com/user-attachments/assets/3a404054-2dfd-4a58-b07a-c7f46488dc0c



<div align="center">

WDoS
Wireless Security Research · Legacy Code Archive
</div>

Overview
WDoS.py is a legacy wireless deauthentication proof of concept. It inspects nearby access-point beacon frames, records advertised network names and access-point addresses, and includes a routine that transmits forged deauthentication frames.
This repository is useful for source-code review, wireless protocol study, and documenting the risks of unprotected management frames. The supplied script is not a passive-only scanner: its main execution path proceeds from discovery to an interactive access-point selection and disruptive transmission.
Use only within an explicitly authorized, isolated wireless lab. Wireless disruptions can extend beyond the intended test devices.

What the code contains
Function	Role
grabssid()	Extracts SSID information and the transmitter address from beacon frames.
displayssid()	Maintains the global access-point dictionary and prints its entries.
sniffall()	Prompts for an interface, attempts a monitor-mode transition, and captures wireless packets.
deauthall()	Constructs deauthentication frames and repeatedly transmits them; supports broadcast or a specified client in its function signature.
closing()	Exits and optionally attempts to stop monitor mode.


The interactive entry point uses the broadcast destination by default. It does not expose a dedicated passive-only mode or a command-line argument parser.
Technical background
Deauthentication is an IEEE 802.11 management operation used to end an authentication relationship. Forged, unprotected management frames can cause compatible clients to disconnect, affecting network availability without recovering a Wi-Fi password.
The script contains no password cracking, credential extraction, persistence, or data-exfiltration logic. Its disruptive behavior is the transmission of deauthentication frames.
Compatibility and dependencies
The source uses Python 2 syntax and APIs, including print statements, raw_input(), and iteritems(). It will not run unchanged under Python 3.
The code references Scapy and the external airmon-ng utility, and assumes a Linux-like environment with suitable wireless hardware and permissions for packet capture and transmission. No dependency versions, supported adapter list, or tested operating-system matrix are provided with the uploaded file.
Known limitations
- Legacy interface assumption: the script assumes the monitor interface will be named mon0 after requesting monitor mode.
- SSID-based storage: access points are stored by SSID, so multiple access points advertising the same name can overwrite one another.
- Incorrect duplicate check: an address is compared against dictionary item tuples rather than a collection of addresses.
- Unvalidated selection: invalid input or an out-of-range selection can terminate execution.
- Transmission interface ambiguity: the selected interface is not explicitly passed to the packet-send calls.
- Unbounded default transmission: the default count does not provide a finite stopping limit.
- Limited cleanup guarantees: broad exception handling and the lack of a guaranteed cleanup block can leave interface state uncertain.
- No channel-management workflow: the code does not implement channel hopping or explicit channel selection.
These observations come from static inspection of the uploaded source. Runtime behavior and hardware compatibility have not been tested.
Defensive research directions
- Document Protected Management Frames (PMF / 802.11w) configuration and client compatibility.
- Study how wireless monitoring systems flag unusual deauthentication activity.
- Compare normal client roaming and disconnect events with suspicious management-frame patterns.
- Build a passive-only Python 3 companion for beacon inventory and offline capture analysis.
- Add source documentation, structured logging, and clear dependency metadata to an archival edition.
- Develop offline tests using synthetic packet fixtures, without transmitting wireless traffic.
Repository contents
File	Description
WDoS.py	Original legacy script.
README.md	Project overview, source review, and defensive research notes.


Attribution and license
The uploaded script contains no author attribution or license declaration. Preserve any original attribution if its provenance is established. No license is assigned by this README; confirm ownership and third-party obligations before adding one.
<div align="center">

Understand the protocol. Document the evidence. Respect the scope.
</div>
