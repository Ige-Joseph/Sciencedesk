# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
import uuid
import google.generativeai as genai
from django.conf import settings



genai.configure(api_key=settings.GEMINI_API_KEY)


@api_view(['POST'])
def sciencedesk_agent(request):
    """
    ScienceDesk - Universal Scientific Assistant
    Handles ALL science/math questions using Gemini AI
    """
    artifact_id = str(uuid.uuid4())
    
    try:
        
        data = request.data
        request_id = data.get("id")
        user_message = data['params']['message']['parts'][0]['text']
        task_id = data['params']['message'].get('taskId', str(uuid.uuid4()))
        
        
        model = genai.GenerativeModel('gemini-2.0-flash-exp')
        
        prompt = f"""You are ScienceDesk, a helpful scientific assistant.

User Question: {user_message}

Provide a clear, accurate answer. You can handle:
- Unit conversions (temperature, length, weight, volume, speed, etc.)
- Math calculations (algebra, calculus, trigonometry, percentages)
- Physics problems (force, energy, velocity, momentum)
- Chemistry calculations (molar mass, concentration, stoichiometry)
- Scientific explanations

Be concise but thorough. Show formulas when relevant. Incase of empty strings
or no text just introduce your self as such """

        
        response = model.generate_content(prompt)
        answer = response.text
        
        
        return Response({
            "jsonrpc": "2.0",
            "id": request_id,
            "result": {
                "id": task_id,
                "contextId": str(uuid.uuid4()),
                "status": {
                    "state": "completed",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                },
                "artifacts": [
                    {
                        "artifactId": artifact_id,
                        "name": "sciencedesk_response",
                        "description": "Scientific answer from ScienceDesk",
                        "parts": [
                            {
                                "kind": "text",
                                "text": answer
                            }
                        ]
                    }
                ],
                "history": [],
                "kind": "task"
            }
        })
        
    except Exception as e:
        
        error_message = f"Sorry, I encountered an error: {str(e)}\n\nPlease try rephrasing your question or ask something else!"
        
        return Response({
            "jsonrpc": "2.0",
            "id": data.get("id", "error"),
            "result": {
                "id": str(uuid.uuid4()),
                "contextId": str(uuid.uuid4()),
                "status": {
                    "state": "completed",
                    "timestamp": datetime.utcnow().isoformat() + "Z",
                },
                "artifacts": [
                    {
                        "role": "agent",
                        "parts": [{"kind": "text", "text": error_message}],
                        "kind": "message"
                    }
                ],
                "history": [],
                "kind": "task"
            }
        })


@api_view(['GET'])
def health_check(request):
    """Health check endpoint"""
    return Response({
        "status": "healthy",
        "agent": "ScienceDesk",
        "version": "1.0.0"
    })

