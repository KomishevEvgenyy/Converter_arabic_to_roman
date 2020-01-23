fetch('conversion:input', {method: 'POST',
    headers: {'Content-type': 'application/json'},
    body: JSON.stringify({pole: 100500})
})