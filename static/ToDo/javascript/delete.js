console.log("loaded");

document.addEventListener("DOMContentLoaded", () => {
    const deleteButtons = document.querySelectorAll(".delete-btn");
    
    deleteButtons.forEach(button => {
      button.addEventListener("click", async (event) => {
        const itemId = event.target.getAttribute("data-id");
        console.log(itemId);
        
  
        try {
          // Remove the item from the DOM
          const itemElement = document.querySelector(`.task-${itemId}`);
          console.log(itemElement);
          
          itemElement.remove();
          console.log("succesfully removed!!");
  
          // Delete the item from the database using AJAX
          await deleteItem(itemId);
          
          alert("Item deleted successfully!");
        } catch (error) {
          console.error("Error deleting item:", error);
          alert("An error occurred while deleting the item.");
        }
      });
    });
  });
  
  // AJAX function to delete item from database
  async function deleteItem(itemId) {
    console.log("calling a method");
    
    const response = await fetch(`http://127.0.0.1:8000/ToDo/delete-item/${itemId}/`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCSRFToken(), // Include CSRF token for security
      },
    });
  
    if (!response.ok) {
      throw new Error("Failed to delete item");
    }
  
    return response.json();
  }
  
  // Function to retrieve CSRF token

    function getCSRFToken() {
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        return csrfToken;
      }
      
         
      
