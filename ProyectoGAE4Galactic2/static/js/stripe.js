// Create a Stripe client

var stripe = Stripe('pk_test_51NsOYSKvLuGizQHh7dyYCsZg5q1FHAmnguP4mI6qoSbfaOuYubzvuRkbufrA6L8IhPi6xTC3yWtOmVkBKy5NMrvV00qLa1U13y');

var Elements = stripe.elements();


var style = {
   base:{
    color: '#32325d',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16',
    '::placeholder': {
        color: '#aab7c4'
    }
},
invalid: {
    color: '#fa755a',
    iconColor: '#fa755a'
}
};

var card = elements.create('card',{style: style});

card.mount('#card-element');

card.addEventListener('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error){
        displayError.textContent = event.error.message;
    } else { 
        displayError.textContent = '';
    }
});

var form = document.getElementById('payment-form');
form.addEventListener('submit', function(event) {
    event.preventDefault();

    stripe.createToken(card).then(function(result) {
        if (result.error) {
            
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            stripeTokenHandler(result.token);
        }
    });
});

function stripeTokenHandler(token) {
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name','stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);


    form.submit();
}

