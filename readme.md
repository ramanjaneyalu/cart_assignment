# Flask Shopping Cart APIs

This repository houses three Flask APIs designed to manage a shopping cart effectively:

1. **Create Shopping Cart API:** Create a new shopping cart and add items to it.

2. **Edit Shopping Cart API:** Edit an existing shopping cart by adding, updating, or removing items.

3. **Summary API:** Obtain a summary of the items within the shopping cart.

## API Endpoints

### 1. Create Shopping Cart

- **Endpoint:** `/cart`
- **HTTP Method:** POST
- **Description:** Create a new shopping cart and populate it with items. After successful creation, it redirects to the summary page.
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
  
### Edit Shopping Cart

- **Endpoint:** `/cart/<int:cart_id>`
- **HTTP Method:** GET (To render the edit form), POST (To submit edited cart data)
- **Description:** Edit an existing shopping cart by adding, updating, or removing items. After editing, it redirects to the summary page.
- **Request Body:** Form data
- **Example Request:**
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

### Summary API

- **Endpoint:** `/summary/<int:cart_id>`
- **HTTP Method:** GET
- **Description:** Retrieve a summary of the items in the shopping cart, including the total price.
- **Example Request:**
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
