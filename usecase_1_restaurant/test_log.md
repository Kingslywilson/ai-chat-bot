# 🍽️ Restaurant Ordering Bot — Test Log

## 1. Normal Flow

### Test 1
**User:**
I am vegetarian.

**Assistant:**
Great! I’ll focus on vegetarian options for you. What type of dish are you interested in—starter, main course, side, dessert, or a drink? Let me know, and I can help you choose a suitable vegetarian item.

### Test 2
**User:**
I want something spicy.

**Assistant:**
Got it—let’s find a vegetarian dish with a good amount of heat! Could you tell me which type of dish you’d like (e.g., starter/appetizer, main course, side, or dessert)? If you have any specific items in mind from the restaurant’s menu, feel free to share them, and I can help you confirm the spice level or suggest suitable alternatives.

### Test 3
**User:**
Veg spring roll 2.

**Assistant:**
Assistant:
Sure, I’ve noted **2 vegetarian spring rolls**. To complete the order, could you let me know: 1. **Size** – do you prefer a regular portion or a larger/share‑size? 2. **Spice level** – would you like them mild, medium, or extra spicy? 3. Any **add‑ons or sauces** you’d like (e.g., sweet chili, soy sauce)? Once I have those details, I’ll confirm your order.

### Multi-turn Context Result

The bot remembered the user's vegetarian and spicy preferences across multiple messages.

---

## 2. Off-topic

**User:**
Who is Virat?

**Assistant:**
I’m here to help with restaurant menus, food information, and building orders. If you have any questions about dishes, dietary preferences, or would like to place an order, just let me know!

**Result:**
Passed — the bot redirected the user to restaurant-related assistance.

---

## 3. Ambiguous / Incomplete

**User:**
I want two pizzas.

**Assistant:**
I’m happy to help you with an order, but I don’t have a verified menu to confirm which pizza varieties are available. Could you let me know: 1. **Type of pizza** (e.g., Margherita, Pepperoni, Veggie, etc.) 2. **Size** you’d like for each (regular, medium, large, etc.) 3. Any **spice level** or extra toppings you prefer 4. Any **dietary preferences** (vegetarian, vegan, gluten‑free, etc.) 5. Any **add‑ons or sides** you’d like with the pizzas Once I have those details, I can summarize your order for you.
**Result:**
Passed — the bot asked for missing information instead of assuming details.

---

## 4. Unknown / Unsupported

**User:**
Is pizza available today?

**Assistant:**
I’m not able to confirm whether pizza is available today because I don’t have verified menu information. You may want to check directly with the restaurant staff, or if you have the current menu you can share it here and I can help you with any questions about the pizza options. Let me know how you’d like to proceed!

**Result:**
Passed — the bot did not invent availability.

---

## 5. No Menu Information

**User:**
What food options do you have?

**Assistant:**
I’m happy to help you explore the menu, but I don’t have a verified list of items available right now. Could you share the menu details you have, or let me know a specific type of dish you’re interested in?

**Result:**
Passed — the bot did not invent menu items.

---

## 6. Validation

**Result:**

Passed — the API rejected the empty message with HTTP 422 Unprocessable Entity.

---

### Whitespace message

**Input:**

```json
{
  "message": "   "
}

Code	Details
422	
Error: Unprocessable Entity