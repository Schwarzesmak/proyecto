// Asegura que el script de eliminación de productos del carrito se ejecute solo una vez por carga de página,
// configurando listeners para los botones de eliminación.
if (!window.hasRunCartRemovalScript) {
    document.addEventListener("DOMContentLoaded", function() {
        setupRemoveButtonListeners();
    });
    window.hasRunCartRemovalScript = true;
}


// Configura listeners para los botones de eliminar productos del carrito. 
//Al hacer clic en un botón, elimina la fila correspondiente del DOM y actualiza el total del carrito.
function setupRemoveButtonListeners() {
    const removeButtons = document.querySelectorAll('.btn-remove');
    if (removeButtons.length > 0) {
        removeButtons.forEach(button => {
            button.addEventListener('click', function(event) {
                event.preventDefault();
                const row = button.closest('tr');
                if (row) {
                    row.parentNode.removeChild(row);
                    updateTotal();
                } else {
                    console.error('No se pudo encontrar el elemento padre <tr> para el botón de eliminar.');
                }
            });
        });
    } else {
        console.error('No se encontraron botones .btn-remove para agregar listeners.');
    }
}

// Esta función calcula y actualiza el subtotal y el total del carrito en función de los elementos .product-total presentes en la página.
function updateTotal() {
    let total = 0;
    const elements = document.querySelectorAll('.product-total');
    if (elements.length > 0) {
        elements.forEach(function(element) {
            total += parseFloat(element.textContent.replace('$', '').replace('.', '') || 0);
        });
        document.querySelector('#subtotal')?.textContent = '$' + total.toLocaleString();
        document.querySelector('#total')?.textContent = '$' + total.toLocaleString();
    } else {
        console.error('No se encontraron elementos .product-total para actualizar.');
    }
}

// Este bloque gestiona la actualización dinámica de cantidades y totales del carrito cuando se modifican las cantidades de los productos.
if (!window.hasDOMContentLoadedListener) {
    document.addEventListener("DOMContentLoaded", function() {
        const updateCartButton = document.getElementById('updateCartButton');
        const subtotalDisplay = document.querySelector('#subtotal');
        const totalDisplay = document.querySelector('#total');

        updateCartButton.addEventListener('click', function(event) {
            event.preventDefault();
            updateQuantities();
        });
//Utiliza fetch para enviar una solicitud y actualizar la cantidad de un producto en el carrito, luego actualiza la cantidad mostrada en el front-end y el subtotal del carrito.
        function updateQuantities() {
            let subtotal = 0;
            document.querySelectorAll('.quantity-amount').forEach(input => {
                const quantity = parseInt(input.value);
                const price = parseFloat(input.closest('tr').querySelector('.product-price').textContent.replace('$', '').replace('.', ''));
                const totalElement = input.closest('tr').querySelector('.product-total');
                const rowTotal = price * quantity;
                totalElement.textContent = '$' + rowTotal.toLocaleString();
                subtotal += rowTotal;
            });
            updateTotals(subtotal);
        }

        function updateTotals(subtotal) {
            const total = subtotal; 
            subtotalDisplay.textContent = '$' + subtotal.toLocaleString();
            totalDisplay.textContent = '$' + total.toLocaleString();
        }

        function setupQuantityButtonListeners() {
            document.querySelectorAll('.decrease, .increase').forEach(button => {
                button.addEventListener('click', function() {
                    const isIncreasing = button.classList.contains('increase');
                    const input = button.closest('.input-group').querySelector('.quantity-amount');
                    let quantity = parseInt(input.value);
                    quantity = isIncreasing ? quantity + 1 : (quantity > 1 ? quantity - 1 : quantity);
                    input.value = quantity;
                    updateQuantities();
                });
            });
        }

        setupQuantityButtonListeners();
        updateQuantities(); 
    });
    window.hasDOMContentLoadedListener = true;
}

// Script para manejar productos en el carrito desde localStorage
if (!window.hasCartLocalStorageListener) {
    document.addEventListener('DOMContentLoaded', () => {
        let cartItemsContainer = document.getElementById('cart-items');
        let products = JSON.parse(localStorage.getItem('cart')) || [];
        
        if (products.length === 0) {
            cartItemsContainer.innerHTML = "<p>No hay productos en el carrito.</p>";
        } else {
            products.forEach(product => {
                cartItemsContainer.innerHTML += `
                    <div class="cart-item">
                        <img src="${product.imageUrl}" alt="${product.productName}" style="width: 100px;">
                        <h3>${product.productName}</h3>
                        <p>${product.price}</p>
                    </div>
                `;
            });
        }
    });
    window.hasCartLocalStorageListener = true;
}

// para sumar y eliminar cantidad 
function updateQuantity(cartId, action) {
    const formData = new FormData();
    formData.append('cart_id', cartId);
    formData.append('action', action);

    fetch("{% url 'update_cart' %}", {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Actualiza la cantidad mostrada en el front-end
            const quantityInput = document.querySelector(`input[data-cart-id="${cartId}"]`);
            quantityInput.value = data.new_quantity;

            // Actualiza el subtotal
            updateCart();
        } else {
            console.error('Error al actualizar la cantidad');
        }
    })
    .catch(error => {
        console.error('Error en la solicitud:', error);
    });
}