// Espera a que el DOM esté cargado
document.addEventListener("DOMContentLoaded", () => {
  // --- Modal de bienvenida ---
  const userModal   = document.getElementById("userModal");
  const userForm    = document.getElementById("userForm");
  const mainContent = document.getElementById("mainContent");

  // Mostrar modal al cargar
  userModal.classList.add("show", "d-block");
  mainContent.classList.add("hidden");

  // Al enviar el formulario del modal
  userForm.addEventListener("submit", (e) => {
    e.preventDefault();

    // Aquí podrías validar o guardar datos si quieres
    // Por ahora, solo ocultamos el modal y mostramos contenido principal
    userModal.classList.remove("show", "d-block");
    userModal.classList.add("hidden");
    mainContent.classList.remove("hidden");
  });

  // Filtrar películas según categoría
  const filterButtons = document.querySelectorAll(".filter-btn");
  const movieCards = document.querySelectorAll(".movie-card");

  filterButtons.forEach(button => {
    button.addEventListener("click", () => {
      const filter = button.getAttribute("data-filter");

      movieCards.forEach(card => {
        if (filter === "all") {
          card.style.display = "block";
        } else {
          if (card.classList.contains(filter)) {
            card.style.display = "block";
          } else {
            card.style.display = "none";
          }
        }
      });
    });
  });

  // Manejo básico del formulario de contacto
  const contactForm = document.getElementById("contactForm");
  contactForm.addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Gracias por contactarnos. Responderemos pronto.");
    contactForm.reset();
  });

  // --- Funcionalidad carrito ---
  const cartList = document.getElementById('cartList');
  const clearCartBtn = document.getElementById('clearCartBtn');

  let cart = [];

  function renderCart() {
    cartList.innerHTML = '';
    if (cart.length === 0) {
      cartList.innerHTML = '<li class="list-group-item">El carrito está vacío.</li>';
    } else {
      cart.forEach((movie, index) => {
        const li = document.createElement('li');
        li.className = 'list-group-item d-flex justify-content-between align-items-center';
        li.textContent = movie;
        
        const removeBtn = document.createElement('button');
        removeBtn.className = 'btn btn-sm btn-danger';
        removeBtn.textContent = 'Eliminar';
        removeBtn.addEventListener('click', () => {
          cart.splice(index, 1);
          renderCart();
        });
        
        li.appendChild(removeBtn);
        cartList.appendChild(li);
      });
    }
  }

  // Añadir evento a los botones "Agregar al carrito"
  document.querySelectorAll('.add-to-cart-btn').forEach(button => {
    button.addEventListener('click', () => {
      const title = button.getAttribute('data-title');
      if (!cart.includes(title)) {
        cart.push(title);
        renderCart();
      } else {
        alert('Esta película ya está en el carrito.');
      }
    });
  });

  clearCartBtn.addEventListener('click', () => {
    cart = [];
    renderCart();
  });

  // Inicializar carrito vacío
  renderCart();
});

