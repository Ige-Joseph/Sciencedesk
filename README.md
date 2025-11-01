# ScienceDesk - AI Scientific Assistant 🔬

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2+-green.svg)](https://www.djangoproject.com/)
[![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange.svg)](https://ai.google.dev/)
[![Deployed on Fly.io](https://img.shields.io/badge/deployed-fly.io-blueviolet)](https://fly.io)

> An intelligent scientific calculator and unit converter for Telex.im, powered by Google Gemini AI. Built for HNG Internship Stage 3.

**🔗 Live Demo:** https://sciencedesk-agent-ancient-pond-7428.fly.dev

**💬 Try on Telex:** `@sciencedesk Convert 100 celsius to fahrenheit`

---

## ✨ Features

- **Unit Conversions** - Temperature, length, weight, volume, speed, pressure, energy
- **Math Calculations** - Algebra, percentages, square roots, trigonometry
- **Physics Problems** - Force, energy, velocity, momentum calculations
- **Chemistry Help** - Molar mass, concentration, stoichiometry
- **Natural Language** - Ask questions casually, no strict syntax required

## 🚀 Quick Start

### Prerequisites
- Python 3.11+

### Installation
```bash
# Clone repository
git clone https://github.com/Ige-Joseph/sciencedesk-ai-agent.git
cd sciencedesk-ai-agent

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key in agent/views.py (line 13)
GEMINI_API_KEY = "your-api-key-here"

# Run server
python manage.py runserver

# Test
curl http://localhost:8000/a2a/health
```

## 🧪 Testing

**Health Check:**
```bash
curl http://localhost:8000/a2a/health
```

**Test Query:**
```bash
curl -X POST http://localhost:8000/a2a/sciencedesk \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "test-1",
    "method": "agent/task",
    "params": {
      "message": {
        "taskId": "task-1",
        "parts": [{"kind": "text", "text": "What is 15% of 350?"}],
        "kind": "message"
      }
    }
  }'
```

**Example Queries:**
```
"Convert 100 celsius to fahrenheit"
"What's 15% of 350?"
"Calculate force if mass is 10kg and acceleration is 5 m/s²"
"How many kilometers is 50 miles?"
"What's the square root of 144?"
```

## 🌐 Deployment (Fly.io)

**Deployed at:** https://sciencedesk-agent-ancient-pond-7428.fly.dev

### Deploy Your Own:
```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login to Fly
fly auth login

# Deploy
fly deploy

# Set API key
fly secrets set GEMINI_API_KEY="your-api-key"
```

## 📡 Telex Integration

1. Go to **AI Coworkers** in Telex.im
2. Create new agent → Switch to **JSON View**
3. Paste this configuration:
```json
{
  "active": true,
  "category": "utilities",
  "name": "sciencedesk",
  "description": "AI-powered scientific calculator and unit converter",
  "long_description": "You are ScienceDesk, an intelligent scientific assistant. You help with unit conversions, math calculations, physics problems, and chemistry computations. Provide clear, accurate answers with explanations.",
  "short_description": "Scientific assistant for calculations and conversions",
  "nodes": [
    {
      "id": "sciencedesk_node",
      "name": "ScienceDesk Assistant",
      "type": "a2a/custom-node",
      "typeVersion": 1,
      "url": "https://sciencedesk-agent-ancient-pond-7428.fly.dev/a2a/sciencedesk",
      "parameters": {},
      "position": [500, 200]
    }
  ],
  "settings": {"executionOrder": "v1"},
  "pinData": {}
}
```

4. Save and activate agent
5. Test: `@sciencedesk Convert 50 miles to km`

**View logs:** `https://api.telex.im/agent-logs/YOUR-CHANNEL-ID.txt`

## 🏗️ Project Structure
```
sciencedesk-ai-agent/
├── agent/
│   ├── views.py          # Agent logic + Gemini integration
│   └── urls.py           # API routing
├── config/
│   ├── settings.py       # Django config
│   └── urls.py           # Main URL routing
├── requirements.txt      # Dependencies
├── fly.toml             # Fly.io config
└── README.md            # Documentation
```

## 🛠️ Tech Stack

- **Backend:** Django 4.2 + Django REST Framework
- **AI:** Google Gemini API (gemini-2.0-flash-exp)
- **Protocol:** A2A (Agent-to-Agent) JSON-RPC 2.0
- **Deployment:** Fly.io
- **Language:** Python 3.11+

## 📚 API Documentation

### Endpoints

#### `POST /a2a/sciencedesk`
Main agent endpoint (A2A protocol)

**Request:**
```json
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "method": "agent/task",
  "params": {
    "message": {
      "taskId": "task-id",
      "parts": [{"kind": "text", "text": "user question"}],
      "kind": "message"
    }
  }
}
```

**Response:**
```json
{
  "jsonrpc": "2.0",
  "id": "request-id",
  "result": {
    "status": {
      "state": "completed",
      "message": {
        "role": "agent",
        "parts": [{"kind": "text", "text": "agent answer"}]
      }
    }
  }
}
```

#### `GET /a2a/health`
Health check endpoint

**Response:** `{"status": "healthy", "agent": "ScienceDesk", "version": "1.0.0"}`

## 🔒 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | ✅ Yes |

## 🤝 Contributing

Contributions welcome! This project was built for HNG Internship Stage 3.

1. Fork the repository
2. Create feature branch: `git checkout -b feature/NewFeature`
3. Commit changes: `git commit -m 'Add NewFeature'`
4. Push: `git push origin feature/NewFeature`
5. Open Pull Request

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/Ige-Joseph/Sciencedesk)
- Built for [HNG Internship](https://hng.tech) Stage 3 Backend

## 🙏 Acknowledgments

- **HNG Internship** - For the challenge and opportunity
- **Telex.im** - For the A2A protocol platform
- **Google Gemini AI** - For natural language processing
- **Fly.io** - For reliable deployment

## 📞 Support


- **Telex Docs:** [docs.telex.im](https://docs.telex.im)

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Built with ❤️ for [HNG Internship](https://hng.tech)

</div>
