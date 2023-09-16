# Flask Shopping Cart APIs

This repository contains three Flask APIs for managing a shopping cart:

1. **Create Shopping Cart** API: Create a new shopping cart and add items to it.

2. **Edit Shopping Cart** API: Edit an existing shopping cart by adding, updating, or removing items.

3. **Summary** API: View a summary of the items in the shopping cart.

## API Endpoints

### 1. Create Shopping Cart

- **Endpoint:** `/cart`
- **HTTP Method:** POST
- **Description:** Create a new shopping cart and add items to it. Redirects to the summary page.
- **Request Body:** JSON
- **Example Request:**
  ```json
  {
    "items": [
      {
        "item": "Product 1",
        "price": 10.99
      },
      {
        "item": "Product 2",
        "price": 19.99
      }
    ]
  }

### Edit Shopping Cart API

**Step 2: Edit Shopping Cart**

- **Endpoint:** `/cart/<int:cart_id>`
- **HTTP Method:** GET (Render the edit form), POST (Submit edited cart data)
- **Description:** Edit an existing shopping cart by adding, updating, or removing items. Redirects to the summary page.
- **Request Body:** Form data

**Example Request (GET):**

- Render the edit form.

**Example Request (POST):**

```json
{
  "items": [
    {
      "item": "Updated Product 1",
      "price": 12.99
    },
    {
      "item": "Product 3",
      "price": 29.99
    }
  ]
}


**Example Response:**

- Redirect to summary page.

### Summary API

**Step 3: View Summary**

- **Endpoint:** `/summary/<int:cart_id>`
- **HTTP Method:** GET
- **Description:** View a summary of the items in the shopping cart, including the total price.

**Example Response:**

```markdown
```json
{
  "cart_id": 1,
  "total_price": 42.97,
  "items": [
    {
      "item": "Updated Product 1",
      "price": 12.99
    },
    {
      "item": "Product 3",
      "price": 29.99
    }
  ]
}
