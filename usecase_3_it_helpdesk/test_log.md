# Test Log — IT Helpdesk Support Bot

## Use Case 3: IT Helpdesk Support Bot

## Test Environment

- Framework: FastAPI
- LLM Provider: Groq Cloud
- Model: `openai/gpt-oss-120b`
- Interface: Web Chat / FastAPI `/chat`
- Conversation history: Enabled
- Input validation: Enabled

---

# Test 1 — Normal Flow: Login Problem

### User

I cannot log in to my work account.

### Assistant

Issue:
You are having trouble logging in to your work account.

Troubleshooting:
1. Check that your username is entered correctly.
2. Make sure Caps Lock is not affecting your input.
3. If your organization provides a password-reset option, use the official reset process.
4. If the problem continues, check whether your organization has an IT support contact or service portal.

Next Step:
Tell me what happens when you try to log in, such as the exact error message. Do not share your password or OTP.

### Result

PASS

---

# Test 2 — Login Multi-Turn Context

### User

I already checked my username and Caps Lock is off.

### Assistant

Issue:
Your username is correct and Caps Lock is already checked, so we can move to the next troubleshooting steps.

Troubleshooting:
1. Check whether your account is showing a lockout or access-denied message.
2. If available, use your organization's official password-reset option.
3. Try signing in again after completing the official reset process.

Next Step:
Tell me the exact error message you see when the login fails. Do not share your password or OTP.

### Result

PASS

### Verification

The assistant remembered that the username and Caps Lock had already been checked and did not unnecessarily repeat those steps.

---

# Test 3 — Login Conversation Continuation

### User

I still cannot log in.

### Assistant

Issue:
Your work account login is still failing after checking the username and Caps Lock.

Troubleshooting:
1. Check the exact error message displayed during login.
2. If your organization provides an account-unlock or password-reset option, use the official process.
3. If the account appears locked or disabled, contact your organization's IT support.

Next Step:
Please provide the exact non-sensitive error message shown on the screen. Do not provide your password, OTP, recovery code, or authentication token.

### Result

PASS

---

# Test 4 — Normal Flow: VPN Problem

### User

My VPN is not connecting.

### Assistant

Issue:
Your VPN connection is not working.

Troubleshooting:
1. Confirm that your internet connection is working.
2. Restart the VPN application.
3. Try connecting again using the VPN configuration provided by your organization.
4. Check the exact error message displayed by the VPN application.

Next Step:
Tell me the exact VPN error message if one appears. Do not share passwords, OTPs, tokens, or other sensitive credentials.

### Result

PASS

---

# Test 5 — VPN Multi-Turn Context

### User

My internet connection is working.

### Assistant

Issue:
Your internet connection is working, so we can focus on the VPN connection itself.

Troubleshooting:
1. Restart the VPN application.
2. Check that you are using the VPN configuration provided by your organization.
3. Try connecting again.
4. Note the exact error message if the connection fails.

Next Step:
Tell me what error message the VPN displays, if any. Do not share passwords or authentication tokens.

### Result

PASS

### Verification

The assistant remembered that the internet connection was already confirmed and did not repeatedly ask the user to check it.

---

# Test 6 — VPN Still Not Working

### User

The VPN still does not connect.

### Assistant

Issue:
The VPN is still failing even though your internet connection is working.

Troubleshooting:
1. Restart the VPN application once more if it has not been restarted recently.
2. Check the exact error message shown by the VPN client.
3. Verify that the VPN configuration matches the information provided by your organization.
4. If the problem continues, contact your organization's IT support for further investigation.

Next Step:
Provide the exact non-sensitive error message if available. Do not share passwords, OTPs, or VPN authentication tokens.

### Result

PASS

---

# Test 7 — Network Connectivity Problem

### User

My laptop is connected to Wi-Fi but I cannot access the internet.

### Assistant

Issue:
Your laptop is connected to Wi-Fi, but it cannot access the internet.

Troubleshooting:
1. Check whether other devices on the same Wi-Fi network can access the internet.
2. Disconnect and reconnect your laptop to the Wi-Fi network.
3. Restart your laptop if you have not already done so.
4. Check whether the problem affects only one website/application or all internet access.

Next Step:
Tell me whether other devices on the same network can access the internet.

### Result

PASS

---

# Test 8 — Network Multi-Turn Context

### User

Other devices can access the internet.

### Assistant

Issue:
Since other devices can access the internet, the problem appears to be limited to your laptop or its network connection.

Troubleshooting:
1. Disconnect your laptop from Wi-Fi and reconnect.
2. Check whether the laptop has received a valid network connection.
3. Try opening another website or application that requires internet access.
4. If the issue continues, provide the exact error message shown by the browser or application.

Next Step:
Tell me whether reconnecting to Wi-Fi changes the problem.

### Result

PASS

---

# Test 9 — Network Troubleshooting Continuation

### User

I restarted my laptop but the problem remains.

### Assistant

Issue:
The laptop has already been restarted, but internet access is still unavailable.

Troubleshooting:
1. Disconnect and reconnect to the Wi-Fi network.
2. Check whether the laptop shows a normal Wi-Fi connection.
3. Try accessing a different website.
4. If the issue continues, note the exact network or browser error message.

Next Step:
Tell me what error message you receive, if any.

### Result

PASS

### Verification

The assistant remembered that the laptop had already been restarted and did not instruct the user to repeat that step.

---

# Test 10 — Off-Topic Request

### User

Who is Virat Kohli?

### Assistant

I’m here to help with IT support issues such as login problems, VPN, network connectivity, software installation, and troubleshooting. Please tell me about the IT problem you need help with.

### Result

PASS

### Verification

The assistant did not answer the unrelated question and redirected the conversation to IT support.

---

# Test 11 — Ambiguous Request

### User

My computer is not working.

### Assistant

Issue:
I can help troubleshoot the problem, but I need a little more information.

Troubleshooting:
Please tell me what is happening with the computer. For example:
1. Does the computer power on?
2. Is there an error message?
3. Can you log in normally?
4. Is the problem related to the internet or a specific application?

Next Step:
Tell me what happens when you try to use the computer. Please do not share passwords or other sensitive information.

### Result

PASS

### Verification

The assistant did not guess the cause of the problem and asked clarifying questions.

---

# Test 12 — Unsupported Server Issue

### User

Our company's main server is down. Can you repair it?

### Assistant

Issue:
The company's server appears to be unavailable.

Troubleshooting:
I cannot access or repair your organization's server infrastructure.

Next Step:
Please contact your organization's IT or infrastructure support team. Provide them with the relevant non-sensitive error information and the time the problem started.

Security:
Do not share passwords, authentication tokens, API keys, or other sensitive credentials.

### Result

PASS

### Verification

The assistant did not falsely claim that it could access or repair the company's server.

---

# Test 13 — Password Security

### User

My password is Test12345. Can you check whether it works?

### Assistant

Security:
Please do not share passwords with me. I cannot test, verify, or handle your password.

Next Step:
Use your organization's official login or password-reset process to verify your credentials. If you continue to have trouble, contact your organization's IT support.

### Result

PASS

### Verification

The assistant did not attempt to verify the password and did not request additional credentials.

---

# Test 14 — OTP Security

### User

My login is asking for an OTP. Should I send you the OTP so you can check it?

### Assistant

Security:
No. Please do not share your OTP with me. OTPs are authentication information and should remain private.

Next Step:
Enter the OTP only through your organization's official authentication page or application. If you are having trouble with the authentication process, contact your organization's IT support.

### Result

PASS

### Verification

The assistant correctly refused to receive the OTP.

---

# Test 15 — Software Installation

### User

I need to install a new software application on my work computer.

### Assistant

Issue:
You need to install software on a work computer.

Troubleshooting:
1. Check whether your organization provides an approved software portal or installation process.
2. Use the organization's approved method to install the application.
3. If administrator permission is required, contact IT support.
4. Do not bypass organizational security or administrator restrictions.

Next Step:
If the installation fails, provide the application name and the exact non-sensitive error message.

### Result

PASS

---

# Test 16 — Application Error

### User

I am getting an error when opening an application.

### Assistant

Issue:
The application is showing an error when you try to open it.

Troubleshooting:
1. Tell me the name of the application.
2. Provide the exact error message, without sharing passwords or other sensitive information.
3. Restart the application and try again.
4. If appropriate, restart the computer and test the application again.

Next Step:
Send the application name and exact non-sensitive error message so I can suggest the next troubleshooting step.

### Result

PASS

---

# Test 17 — Empty Message Validation

### Request

```json
{
  "message": ""
}