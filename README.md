# Multi-Client Chat Application

A simple yet robust real-time chat application built with Python using TCP sockets and threading. This application supports multiple concurrent clients with real-time message broadcasting and username handling.

## 🚀 Features

- **Multi-client support**: Handle multiple users simultaneously
- **Real-time messaging**: Instant message delivery to all connected clients
- **Username registration**: Each client connects with a unique username
- **Broadcast messaging**: Messages are sent to all connected clients except the sender
- **Join/Leave notifications**: Users are notified when others join or leave
- **Graceful disconnection**: Clean exit with `/quit` command
- **Cross-platform**: Works on Windows, macOS, and Linux

## Tech Stack

- **Language**: Python 3.x
- **Core Libraries**: 
  - `socket` - TCP network communication
  - `threading` - Concurrent client handling
  - `argparse` - Command-line argument parsing
  - `sys` - System-specific parameters

## 📋 Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only built-in libraries)

## 📁 Project Structure

```
chat-application/
├── server.py          # Server implementation
├── client.py          # Client implementation
├── README.md          # This file
└── requirements.txt   # Dependencies (optional)
```

## Quick Start

### 1. Start the Server

```bash
python server.py
```

The server will start listening on `0.0.0.0:5000` by default and display:
```
Server listening on 0.0.0.0:5000
```

### 2. Connect Clients

Open new terminal windows/tabs for each client:

```bash
# Client 1
python client.py --name Alice

# Client 2  
python client.py --name Bob

# Client 3
python client.py --name Charlie
```

### 3. Start Chatting!

- Once connected, you'll see: `Connected to server. You can start typing messages.`
- Type your message and press Enter to send
- All other connected clients will receive your message
- Type `/quit` to disconnect from the server

##  Usage Examples

### Basic Usage
```bash
# Start server (default: 0.0.0.0:5000)
python server.py

# Connect client with username
python client.py --name John
```

### Custom Server Configuration
```bash
# Server runs on all interfaces (0.0.0.0) port 5000
# To change server settings, modify the main() function in server.py:
# host = "127.0.0.1"  # localhost only
# port = 8080         # custom port
```

### Client Connection Options
```bash
# Connect to localhost (default)
python client.py --name Alice

# Connect to custom host and port
python client.py --host 192.168.1.100 --port 8080 --name Alice

# Connect to remote server
python client.py --host example.com --port 5000 --name Alice
```

##  Configuration

### Server Configuration
Edit the `main()` function in `server.py`:

```python
def main():
    host = "0.0.0.0"      # Listen on all interfaces
    port = 5000           # Port number
    # ... rest of the code
```

### Client Configuration
Use command-line arguments:

| Argument | Default | Description |
|----------|---------|-------------|
| `--host` | `127.0.0.1` | Server IP address |
| `--port` | `5000` | Server port number |
| `--name` | Required | Your username |

##  Network Architecture

```
┌─────────────────┐         ┌──────────────────┐
│   Client Harsh  │◄───────►│                  │
├─────────────────┤         │                  │
│    Client Bob   │◄───────►│   Server (TCP)   │
├─────────────────┤         │   Port: 5000     │
│  Client Charlie │◄───────►│                  │
└─────────────────┘         └──────────────────┘
```

##  Commands

| Command | Description |
|---------|-------------|
| `<message>` | Send message to all connected users |
| `/quit` | Disconnect from the server |

##  How It Works

### Server Workflow
1. **Initialization**: Creates TCP socket and binds to host:port
2. **Listening**: Waits for incoming client connections
3. **Connection Handling**: For each new client:
   - Accepts connection
   - Creates new thread to handle client
   - Receives and stores username
   - Broadcasts join notification
4. **Message Handling**: 
   - Receives messages from clients
   - Broadcasts to all other connected clients
   - Handles client disconnections

### Client Workflow  
1. **Connection**: Connects to server using TCP socket
2. **Authentication**: Sends username to server
3. **Threading**: Creates separate thread for receiving messages
4. **Communication**: 
   - Main thread handles user input and sends messages
   - Receiver thread continuously listens for incoming messages
5. **Disconnection**: Clean exit with `/quit` command

##  Testing

### Test Scenario 1: Basic Messaging
1. Start server: `python server.py`
2. Connect 2 clients: 
   - Terminal 1: `python client.py --name Alice`
   - Terminal 2: `python client.py --name Bob`
3. Send messages from both clients
4. Verify messages appear in both terminals

### Test Scenario 2: Multiple Clients
1. Connect 5+ clients with different names
2. Send messages from various clients
3. Verify all clients receive all messages
4. Test joining/leaving notifications

### Test Scenario 3: Connection Handling
1. Connect clients, then close some terminal windows abruptly
2. Verify server handles disconnections gracefully
3. Verify remaining clients continue to work normally

##  Troubleshooting

### Common Issues

**"Address already in use" Error**
```bash
# Kill process using the port
sudo lsof -ti:5000 | xargs kill -9

# Or change port in server.py
port = 5001  # Use different port
```

**"Connection refused" Error**
- Ensure server is running before connecting clients
- Check if firewall is blocking the connection
- Verify host and port settings

**Client disconnects unexpectedly**
- Check network connectivity
- Monitor server console for error messages
- Ensure server has sufficient resources

##  Security Considerations

- Input validation and sanitization
- Message encryption
- User authentication
- Rate limiting
- Message size limits
- Proper error logging

##  Performance Notes

- **Concurrent Clients**: Limited by system threading capacity
- **Message Size**: Currently limited to 1024 bytes per message
- **Memory Usage**: Minimal - stores only active client connections
- **Network Protocol**: TCP ensures reliable message delivery