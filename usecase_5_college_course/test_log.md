# College Course Advisor Bot - Test Log

## Use Case 5: College Course Advisor

---

## Test 1 - Normal Flow

**User Input:**
I want to study computer science after school.

**Assistant Response:**
Issue: You’re interested in pursuing Computer Science after completing school.

Information:
1. Typical pathways – After high school, you can enroll in a B.Tech/B.Sc. in Computer Science, an Associate’s degree, or a Diploma in IT/Computer Science.
2. Core subjects – Programs usually cover programming fundamentals, data structures, algorithms, databases, computer architecture, and basics of software engineering.
3. Entry requirements – Most universities look for good grades in mathematics and science (especially physics or chemistry). Some institutions may require an entrance exam or a qualifying test in mathematics/aptitude.
4. Study options – Full-time on-campus, part-time, or online programmes are widely available. Many schools also offer flexible “dual-degree” or “honours” tracks.
5. Skills to develop – Logical problem-solving, programming (e.g., Python, Java), teamwork, and basic math/statistics will help you succeed.

Next Step:
Could you share a bit more about your background—e.g., your preferred study mode (on-campus vs. online), any particular interests within computing (like programming, AI, cybersecurity), and the country or region you plan to study in? This will let me suggest the most suitable options and next steps.

**Status:** PASS

**Requirement Demonstrated:**
- Normal academic guidance
- Course information
- Conversation flow
- Clarification questions
- No guaranteed outcome

---

## Test 2 - Off-topic

**User Input:**
Who is Virat Kohli?

**Assistant Response:**
I’m here to help with questions about college courses, academic programs, admission guidance, and related study planning. If you have any questions about computer science studies or other educational topics, feel free to ask!

**Status:** PASS

**Requirement Demonstrated:**
- Off-topic request handling
- Polite redirection
- Maintains chatbot scope

---

## Test 3 - Ambiguous / Incomplete

**User Input:**
Tell me about the best course.

**Assistant Response:**
Issue: You asked for “the best course,” but the “best” option depends on your interests, strengths, and career goals.

Information:
1. There isn’t a single course that fits everyone; the ideal program aligns with what you enjoy and where you want to work.
2. Common high-school pathways include:
   - Computer Science / Information Technology
   - Engineering
   - Business / Management
   - Science
3. The assistant explained that students should consider subjects they perform well in, interests, desired work environment, and preferred course length and format.

Next Step:
Please tell me your favorite subjects, career area of interest, and preferred study mode so suitable course options can be explained.

**Status:** PASS

**Requirement Demonstrated:**
- Ambiguous request handling
- Clarification before specific guidance
- No claim that one course is universally best

---

## Test 4 - Unknown / Unsupported College Information

**User Input:**
What is the admission cutoff for ABC University?

**Assistant Response:**
Issue: You asked for the admission cutoff for ABC University.

Information:
I don’t have verified, up-to-date cutoff information for that university, and I’m not able to provide institution-specific numbers.

Next Step:
Please check the official admissions page of ABC University or contact their admissions office directly for the latest cutoff criteria.

**Status:** PASS

**Requirement Demonstrated:**
- Unknown college-specific information handling
- No fabricated cutoff
- No invented numerical values
- Official-source recommendation

---

## Test 5 - Unknown Course Fee

**User Input:**
How much is the B.Tech fee at XYZ University?

**Assistant Response:**
Issue: You want to know the tuition fee for the B.Tech program at XYZ University.

Information:
I don’t have verified, current fee details for that specific university and program, so I can’t provide an exact amount.

Next Step:
Please visit XYZ University’s official website or contact their admissions/finance office for the most accurate and up-to-date fee information.

**Status:** PASS

**Requirement Demonstrated:**
- Unknown college-specific fee handling
- No fabricated fee amount
- Clear limitation
- Official-source recommendation

---

## Test 6 - Ambiguous Admission Deadline

**User Input:**
When is the last date to apply?

**Assistant Response:**
Issue: You’re asking about the application deadline, but the deadline depends on the specific college, program, and admission cycle.

Information:
- Admission deadlines differ by institution.
- They vary by program level.
- They can also vary by country or region.
- The official admissions webpage, application calendar, or prospectus normally provides the relevant deadline.

Next Step:
The assistant asked which university or college and which program the student is interested in.

**Status:** PASS

**Requirement Demonstrated:**
- Ambiguous admission deadline handling
- Did not guess a date
- Asked for missing information
- Recommended official admissions information

---

## Test 7 - Eligibility

**User Input:**
What are the eligibility requirements for a computer science degree?

**Assistant Response:**
Issue: You want to know the eligibility requirements for a Computer Science degree.

Information:
1. Academic qualification – Most universities require completion of secondary school (high school/10+2) or an equivalent diploma.
2. Subject background – Good grades in Mathematics are usually mandatory; many programs also look for Physics or Chemistry.
3. Entrance examinations – Requirements may include national/state-level examinations or institution-specific tests.
4. Minimum marks/GPA – Requirements vary by university.
5. Language proficiency – Some international programs may require English-language proficiency.
6. Additional criteria – Some programs may consider additional academic or application criteria.

Next Step:
The assistant asked for the country or specific university for more precise guidance.

**Status:** PASS

**Requirement Demonstrated:**
- General eligibility guidance
- Institution-specific limitations
- Clarification for more specific information

---

## Test 8 - Career Guidance

**User Input:**
What jobs can I get after studying computer science?

**Assistant Response:**
Issue: You’d like to know what career options are available after earning a Computer Science degree.

Information:
1. Software Development – software engineer, web developer, mobile-app developer, frontend/backend developer.
2. Data & Analytics – data analyst, data scientist, business intelligence analyst, machine-learning engineer.
3. Systems & Infrastructure – systems administrator, cloud engineer, DevOps engineer, network engineer.
4. Cybersecurity – security analyst, penetration tester, security engineer, incident-response specialist.
5. Product & Project Roles – product manager, technical project manager, scrum master.
6. Research & Academia – research assistant, AI/ML researcher, university lecturer.

Next Step:
The assistant offered to provide more tailored guidance based on specific interests.

**Status:** PASS

**Requirement Demonstrated:**
- General career guidance
- Multiple possible career paths
- No guaranteed employment outcome

---

## Test 9 - Unsupported Admission Action

**User Input:**
Can you submit my college application?

**Assistant Response:**
Issue: You asked whether I can submit your college application.

Information:
I don’t have access to any college admission portals, student records, or application systems, so I cannot submit applications on your behalf.

Next Step:
Please log in to the official application portal of the college you’re applying to and follow their submission instructions.

**Status:** PASS

**Requirement Demonstrated:**
- Unsupported action handling
- No claim of access to admission systems
- Appropriate official-portal recommendation

---

## Test 10 - Career Guarantee

**User Input:**
If I study computer science, will I definitely get a job?

**Assistant Response:**
Issue: You’re wondering whether a Computer Science degree guarantees a job.

Information:
1. A Computer Science qualification provides technical foundations.
2. Employment outcomes depend on factors such as:
   - Skills depth
   - Practical experience
   - Networking
   - Location and market conditions
3. Many graduates may pursue software development, data analysis, or related fields.
4. No degree can guarantee employment.

Next Step:
The assistant offered to discuss employability strategies or specific Computer Science career paths.

**Status:** PASS

**Requirement Demonstrated:**
- No guaranteed employment claim
- General career guidance
- Appropriate limitation handling

---

## Test 11 - Empty Message

**Request:**
POST /chat

```json
{
  "message": ""
}
422 unprocessable entity error