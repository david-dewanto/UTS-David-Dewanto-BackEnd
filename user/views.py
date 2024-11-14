from django.http import JsonResponse
import json
from django.shortcuts import render
import pyrebase
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'apiKey': os.getenv('FIREBASE_API_KEY'),
    'authDomain': os.getenv('FIREBASE_AUTH_DOMAIN'),
    'databaseURL': os.getenv('FIREBASE_DATABASE_URL'),
    'projectId': os.getenv('FIREBASE_PROJECT_ID'),
    'storageBucket': os.getenv('FIREBASE_STORAGE_BUCKET'),
    'messagingSenderId': os.getenv('FIREBASE_MESSAGING_SENDER_ID'),
    'appId': os.getenv('FIREBASE_APP_ID'),
    'measurementId': os.getenv('FIREBASE_MEASUREMENT_ID')
}


firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@csrf_exempt
def postSign(request):
    if request.method == "OPTIONS":
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    if request.method == 'POST':
        try:
            print("Received request headers:", request.headers)
            print("Received request body:", request.body.decode('utf-8'))
            
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            
            print(f"Attempting login with email: {email}")
            
            user = auth.sign_in_with_email_and_password(email, password)
            
            response = JsonResponse({
                'status': 'success',
                'token': user['idToken']
            })
            
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
            
            return response
            
        except Exception as e:
            print(f"Login error: {str(e)}")
            response = JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
            
            response["Access-Control-Allow-Origin"] = "*"
            return response

    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed'
    }, status=405)

@csrf_exempt
def register(request):
    if request.method == "OPTIONS":
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            
            print(f"Attempting registration with email: {email}")
            
            user = auth.create_user_with_email_and_password(email, password)
            
            response = JsonResponse({
                'status': 'success',
                'message': 'Registration successful',
            })
            
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
            
            return response
            
        except Exception as e:
            print(f"Registration error: {str(e)}")
            response = JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
            
            response["Access-Control-Allow-Origin"] = "*"
            return response
        
@csrf_exempt
def forgotPassword(request):
    if request.method == "OPTIONS":
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            
            print(f"Attempting password reset for email: {email}")
            
            auth.send_password_reset_email(email)
            
            response = JsonResponse({
                'status': 'success',
                'message': 'Password reset email sent successfully'
            })
            
            response["Access-Control-Allow-Origin"] = "*"
            response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
            response["Access-Control-Allow-Headers"] = "Content-Type"
            
            return response
            
        except Exception as e:
            print(f"Password reset error: {str(e)}")
            response = JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
            
            response["Access-Control-Allow-Origin"] = "*"
            return response

    return JsonResponse({
        'status': 'error',
        'message': 'Method not allowed'
    }, status=405)

db = firebase.database()

@csrf_exempt
def getProgress(request):
    if request.method == 'POST':
        try:
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                response = JsonResponse({
                    'status': 'error',
                    'message': 'No valid authorization token provided'
                }, status=401)
                response["Access-Control-Allow-Origin"] = "*"
                return response

            token = auth_header.split(' ')[1]
            
            decoded_token = auth.get_account_info(token)
            user_id = decoded_token['users'][0]['localId']

            # Create a new database instance with the token
            db = firebase.database()
            db.credentials = {'token': token}  # Changed this line

            data = json.loads(request.body)
            
            progress = db.child("users").child(user_id).child("progress").get(token=token)  # Added token parameter

            if (progress.val()):
                progress_data = progress.val()
            else:
                progress_data = save_initial_progress(user_id, data.get('timestamp'), token)  # Pass token to save_initial_progress
            
            response = JsonResponse({
                'status': 'success',
                'progress': progress_data
            })
            
            response["Access-Control-Allow-Origin"] = "*"
            return response
            
        except Exception as e:
            print(f"Error retrieving progress: {str(e)}")
            response = JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
            response["Access-Control-Allow-Origin"] = "*"
            return response

def save_initial_progress(user_id, timestamp, token):  # Added token parameter
    progress_data = {
        'module': 1,
        'part': 1,
        'subpart': 1,
        'timestamp': timestamp
    }
    db = firebase.database()
    db.credentials = {'token': token}
    db.child("users").child(user_id).child("progress").set(progress_data, token=token)  # Added token parameter
    return progress_data

@csrf_exempt
def saveProgress(request):
    if request.method == 'POST':
        try:
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                response = JsonResponse({
                    'status': 'error',
                    'message': 'No valid authorization token provided'
                }, status=401)
                response["Access-Control-Allow-Origin"] = "*"
                return response

            token = auth_header.split(' ')[1]
            
            decoded_token = auth.get_account_info(token)
            user_id = decoded_token['users'][0]['localId']

            # Create a new database instance with the token
            db = firebase.database()
            db.credentials = {'token': token}  # Changed this line

            data = json.loads(request.body)
            progress_data = {
                'module': data.get('module'),
                'part': data.get('part'),
                'subpart': data.get('subpart'),
                'timestamp': data.get('timestamp')
            }
            
            db.child("users").child(user_id).child("progress").set(progress_data, token=token)  # Added token parameter
            
            response = JsonResponse({
                'status': 'success',
                'message': 'Progress saved successfully'
            })
            
            response["Access-Control-Allow-Origin"] = "*"
            return response
            
        except Exception as e:
            print(f"Error saving progress: {str(e)}")
            response = JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=400)
            response["Access-Control-Allow-Origin"] = "*"
            return response