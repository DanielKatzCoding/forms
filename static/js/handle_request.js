async function submitForm() {
    const form = document.getElementById('form_id');

    const formData = new FormData(form);

    // Convert FormData to a JSON object
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    const wrapper = {};
    wrapper[document.getElementById('section_id').textContent] = data;
    const path = window.location.pathname;
    wrapper['page_name'] = path.split('/').pop();

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(wrapper),
        });

        if (response.redirected) {
            // Perform the redirection on the client side
            window.location.href = response.url;
        } else {
            const result = await response.json();
            document.getElementById('response').innerText = JSON.stringify(result);
        }
    } catch (error) {
        console.error('Error submitting form:', error);
        document.getElementById('response').innerText = 'An error occurred.';
    }
}
