# stcp-next-bus

Small script that tells me when the next that takes me home available. This searches for a bus in a given line on a given stop.

I find the output is particularly useful to populate a widget, for instance, next to your clock:

![Example usage](./example.png)

## Usage

Install the dependencies and run the script as a standard Python file, providing the line number and the stop code.
```bash
pip install -r requirements.txt
python stcp_next_bus.py <line> <stop-code>
```

For a more practical use, I have added the script to my local binaries as an executable, allowing me to run it with more flexibility.
```bash
chmod +x stcp_next_bus.py
cp stcp_next_bus.py ~/.local/bin/next_bus  # ~/.local/bin/ is added to path
next_bus 600 ASZ2
```
