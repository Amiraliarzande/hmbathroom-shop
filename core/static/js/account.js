(function () {
  var money = new Intl.NumberFormat("en-GB", { style: "currency", currency: "GBP" });

  document.querySelectorAll("[data-static-form]").forEach(function (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      if (!form.reportValidity()) return;
      var button = form.querySelector('button[type="submit"]');
      if (!button) return;
      var original = button.textContent;
      button.textContent = "Saved in preview";
      button.disabled = true;
      window.setTimeout(function () {
        button.textContent = original;
        button.disabled = false;
      }, 1800);
    });
  });

  var addressForm = document.getElementById("address-form");
  var addAddress = document.querySelector("[data-show-address]");
  
  if (addressForm && addAddress) {
    addAddress.addEventListener("click", function () {
      addressForm.hidden = false;
      addressForm.querySelector("input").focus();
      addressForm.scrollIntoView({ behavior: "smooth", block: "start" });
    });
    
    var cancel = document.querySelector("[data-cancel-address]");
    if (cancel) {
      cancel.addEventListener("click", function () {
        addressForm.reset();
        addressForm.hidden = true;
      });
    }


    document.querySelectorAll("[data-edit-address]").forEach(function (button) {
      button.addEventListener("click", function () {
        addressForm.hidden = false;
        addressForm.querySelector("input").focus();
        addressForm.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  var cart = document.getElementById("cart-items");
  if (cart) {
    function updateCart() {
      var subtotal = 0;
      cart.querySelectorAll(".cart-item").forEach(function (item) {
        var price = Number(item.getAttribute("data-price")) || 0;
        var quantity = item.querySelector("[data-quantity]");
        var count = Math.max(1, Math.min(99, Number(quantity.value) || 1));
        quantity.value = count;
        var total = price * count;
        subtotal += total;
        item.querySelector(".item-total").textContent = money.format(total);
      });
      var subtotalNode = document.getElementById("cart-subtotal");
      var totalNode = document.getElementById("cart-total");
      var deliveryNode = document.getElementById("cart-delivery");
      if (subtotalNode) subtotalNode.textContent = money.format(subtotal);
      if (totalNode) totalNode.textContent = money.format(subtotal);
      if (deliveryNode) deliveryNode.textContent = subtotal >= 250 ? "Free (demo)" : "Calculated next";
      var count = Array.from(cart.querySelectorAll("[data-quantity]")).reduce(function (sum, input) {
        return sum + (Number(input.value) || 0);
      }, 0);
      document.querySelectorAll(".cart-count").forEach(function (node) { node.textContent = count; });
      if (!cart.querySelector(".cart-item")) {
        cart.innerHTML = '<div class="empty-state"><div class="empty-icon">▱</div><h3>Your basket is empty</h3><p>Explore the range and add something to your basket.</p><a class="account-btn" href="products.html">Browse products</a></div>';
      }
    }
    cart.addEventListener("click", function (event) {
      var qtyButton = event.target.closest("[data-qty]");
      if (qtyButton) {
        var input = qtyButton.parentElement.querySelector("[data-quantity]");
        input.value = Math.max(1, Math.min(99, (Number(input.value) || 1) + Number(qtyButton.getAttribute("data-qty"))));
        updateCart();
      }
      var remove = event.target.closest("[data-remove-item]");
      if (remove) {
        event.preventDefault();
        remove.closest(".cart-item").remove();
        updateCart();
      }
    });
    cart.addEventListener("change", function (event) {
      if (event.target.matches("[data-quantity]")) updateCart();
    });
    updateCart();
  }

  var filter = document.querySelector("[data-filter-orders]");
  if (filter) {
    filter.addEventListener("change", function () {
      document.querySelectorAll("[data-order-status]").forEach(function (row) {
        row.hidden = filter.value !== "all" && row.getAttribute("data-order-status") !== filter.value;
      });
    });
  }

  var authSwitch = document.getElementById("auth-switch");
  if (authSwitch) {
    authSwitch.addEventListener("click", function (event) {
      event.preventDefault();
      var signup = authSwitch.getAttribute("href") === "#signup";
      authSwitch.setAttribute("href", signup ? "#signin" : "#signup");
      document.getElementById("auth-title").textContent = signup ? "Create your account" : "Sign in to your account";
      document.getElementById("auth-description").textContent = signup ? "Create an account to track orders and save your delivery details." : "Access your orders, saved addresses and account details.";
      document.getElementById("auth-submit").textContent = signup ? "Create account" : "Sign in";
      document.getElementById("auth-switch-copy").textContent = signup ? "Already have an account?" : "New to HM Bathroom?";
      authSwitch.textContent = signup ? "Sign in" : "Create an account";
      document.getElementById("auth-password").autocomplete = signup ? "new-password" : "current-password";
    });
  }
})();