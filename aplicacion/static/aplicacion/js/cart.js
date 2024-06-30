// Asegúrate de que el script no se ejecute más de una vez
if (!window.hasRunCartRemovalScript) {
    document.addEventListener("DOMContentLoaded", function() {
        // Aquí va tu función setupRemoveButtonListeners()
        setupRemoveButtonListeners();
    });
    window.hasRunCartRemovalScript = true;
}

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

// Función para actualizar el total del carrito
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


if (!window.hasDOMContentLoadedListener) {
    document.addEventListener("DOMContentLoaded", function() {
        const updateCartButton = document.getElementById('updateCartButton');
        const subtotalDisplay = document.querySelector('#subtotal');
        const totalDisplay = document.querySelector('#total');

        updateCartButton.addEventListener('click', function(event) {
            event.preventDefault();
            updateQuantities();
        });

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
            const total = subtotal; // You can add taxes, discounts, etc. here if needed
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
        updateQuantities(); // Calculate the initial total when the page loads
    });
    window.hasDOMContentLoadedListener = true;
}

if (!window.hasDOMContentLoadedListener) {
    document.addEventListener("DOMContentLoaded", function() {
        const decreaseButtons = document.querySelectorAll('.decrease');
        const increaseButtons = document.querySelectorAll('.increase');
        const totalDisplay = document.querySelector('.text-black strong');

        function updateTotal() {
            let total = 0;
            document.querySelectorAll('.product-total').forEach(function(element) {
                total += parseFloat(element.textContent.replace('$', '').replace('.', ''));
            });
            totalDisplay.textContent = '$' + total.toLocaleString();
        }

        function setupButtonListeners() {
            decreaseButtons.forEach(button => {
                button.removeEventListener('click', handleDecrease);
                button.addEventListener('click', handleDecrease);
            });

            increaseButtons.forEach(button => {
                button.removeEventListener('click', handleIncrease);
                button.addEventListener('click', handleIncrease);
            });
        }

        function handleDecrease(event) {
            const input = this.parentNode.parentNode.querySelector('.quantity-amount');
            let quantity = parseInt(input.value);
            if (quantity > 1) {
                quantity--;
                input.value = quantity;
                const price = parseFloat(this.closest('tr').querySelector('.product-price').textContent.replace('$', '').replace('.', ''));
                this.closest('tr').querySelector('.product-total').textContent = '$' + (price * quantity).toLocaleString();
                updateTotal();
            } else if (quantity === 1) {
                alert("La cantidad mínima permitida es 1. No puedes disminuir la cantidad más.");
                // Aquí puedes agregar cualquier otra acción que desees tomar cuando la cantidad es 1
            } else {
                // Si la cantidad es menor que 1, establecemos la cantidad a 1
                quantity = 1;
                input.value = quantity;
                const price = parseFloat(this.closest('tr').querySelector('.product-price').textContent.replace('$', '').replace('.', ''));
                this.closest('tr').querySelector('.product-total').textContent = '$' + (price * quantity).toLocaleString();
                updateTotal();
            }
        }

        function handleIncrease(event) {
            const input = this.parentNode.parentNode.querySelector('.quantity-amount');
            let quantity = parseInt(input.value);
            quantity++;
            input.value = quantity;
            const price = parseFloat(this.closest('tr').querySelector('.product-price').textContent.replace('$', '').replace('.', ''));
            this.closest('tr').querySelector('.product-total').textContent = '$' + (price * quantity).toLocaleString();
            updateTotal();
        }

        setupButtonListeners();
    });
    window.hasDOMContentLoadedListener = true;
}

if (!window.hasDOMContentLoadedListener) {
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
    window.hasDOMContentLoadedListener = true;
}
