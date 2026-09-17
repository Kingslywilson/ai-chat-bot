# Use Case 2 - Movie Ticket Booking Bot
## Test Log

### Normal Flow

#### Test 1 - Start Booking

**User:**
> I want to book movie tickets.

**Assistant:**
> Sure! I can help you with that. Which movie would you like to watch, and in which city?

**Result:** PASS

The assistant identified the movie-ticket booking intent and asked for the missing movie and city details.

---

#### Test 2 - Provide City

**User:**
> I want to watch a movie in Chennai.

**Assistant:**
> Got it—Chennai it is. What movie would you like to see, and on which date?

**Result:** PASS

The assistant remembered the city and asked for the missing movie and date.

---

#### Test 3 - Provide Date/Time Preference

**User:**
> Saturday evening.

**Assistant:**
> Great! To finalize the details, could you let me know:
> 1. Movie name you’d like to watch
> 2. Which Saturday you’re planning for
> 3. Preferred evening showtime
> 4. Number of tickets you need
> 5. Desired seat category

**Result:** PASS

The assistant recognized the evening preference and asked for the remaining required booking information instead of guessing.

---

#### Test 4 - Multi-turn Context

**User:**
> I want 2 tickets. avatar

**Assistant:**
> Got it—2 tickets for Avatar in Chennai. I just need a couple more details to complete the summary:
> 1. Date – which Saturday are you planning to go?
> 2. Evening showtime – what time do you prefer?
> 3. Seat category – which would you like?

**Result:** PASS

The assistant correctly remembered the previously provided city, as well as the movie and ticket quantity from the current conversation. It asked for the remaining information.

---

### Multi-turn Conversation / Context Memory

**Conversation:**

**User:**
> I want to book movie tickets.

**Assistant:**
> Sure! I can help you with that. Which movie would you like to watch, and in which city?

**User:**
> I want to watch a movie in Chennai.

**Assistant:**
> Got it—Chennai it is. What movie would you like to see, and on which date?

**User:**
> Saturday evening.

**Assistant:**
> Great! To finalize the details, could you let me know:
> 1. Movie name you’d like to watch
> 2. Which Saturday you’re planning for
> 3. Preferred evening showtime
> 4. Number of tickets you need
> 5. Desired seat category

**User:**
> I want 2 tickets. avatar

**Assistant:**
> Got it—2 tickets for Avatar in Chennai. I just need a couple more details to complete the summary:
> 1. Date – which Saturday are you planning to go?
> 2. Evening showtime – what time do you prefer?
> 3. Seat category – which would you like?

**Result:** PASS

The assistant demonstrated multi-turn context by remembering the city and combining information provided across previous messages.

---

### Failure Mode 1 - Off-topic Request

**User:**
> Who is Virat Kohli?

**Assistant:**
> I’m here to help with movie-ticket information such as showtimes, theatres, seat categories, and bookings. If you have any questions about movies or need assistance with tickets, just let me know!

**Result:** PASS

The assistant did not answer the unrelated question and redirected the conversation back to movie-ticket assistance.

---

### Failure Mode 2 - Ambiguous / Incomplete Request

**User:**
> I want to book tickets.

**Assistant:**
> Great! I can help you with that. To get started, could you tell me:
> 1. Which movie you’d like to watch, and
> 2. Which city you’ll be attending in?

**Result:** PASS

The request was incomplete, so the assistant asked for the missing movie and city information instead of making assumptions.

---

### Failure Mode 3 - Unknown / Unsupported Information

**User:**
> Is the 9:30 PM show available tomorrow?

**Assistant:**
> I’m not able to confirm showtime availability without a few more details. Could you let me know:
> - Which movie you’d like to see,
> - The city (and theatre, if you have one in mind), and
> - The exact date you’re referring to (instead of "tomorrow," please provide the calendar date)?
> Once I have that information, I can let you know whether the 9:30 PM show is an option.

**Result:** PASS

The assistant did not invent showtime availability and requested the required information.

---

### Test - Unknown Ticket Pricing

**User:**
> How much is a movie ticket?

**Assistant:**
> I don’t have verified pricing information for a ticket without knowing the specific movie, city (and theatre), date, showtime, and seat category you’re interested in. Could you provide those details? Once I have that information, I can let you know that I’m unable to confirm the exact price and suggest checking the theatre’s official booking site for current rates.

**Result:** PASS

The assistant did not invent a ticket price and clearly indicated that it could not confirm the exact price.

---

### Test - Unknown Current Movie Listings

**User:**
> What movies are playing today?

**Assistant:**
> I’m not able to list the movies that are playing without knowing where you’d like to watch them. Could you let me know:
> - The city (and, if you have a specific theatre in mind) where you’d like to see a film, and
> - The date you’re interested in?
> With that information I can let you know that I don’t have verified listings and suggest checking the local theatre’s website or a ticket-booking platform for the current show lineup.

**Result:** PASS

The assistant did not invent current movie listings and directed the user toward verified sources.

---

### Test - No Fake Booking

**User:**
> Book 2 tickets for me now.

**Assistant:**
> Sure, I can help you gather the details for your booking. To proceed, I need the following information:
> 1. Movie name – which film would you like to watch?
> 2. City (and theatre, if you have a preference) – where will you be attending?
> 3. Date – the calendar date you’d like to see the movie?
> 4. Showtime – what time would you prefer?
> 5. Seat category – standard, premium, VIP, etc.
> Once I have these details, I’ll summarize everything for you to confirm before any booking step.

**Result:** PASS

The assistant did not falsely claim that tickets had been booked. It requested the required information and stated that it would summarize the booking before any booking step.

---

### Validation Test

#### Empty Message

**Request:**

```json
{
  "message": ""
}
**Response**
422 Unprocessable Entity