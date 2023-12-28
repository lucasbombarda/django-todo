document.addEventListener('DOMContentLoaded', () => {
    const main = new Messages();
    main.init();
})

class Messages {
    constructor() {}

    init() {
        const messages = document.querySelectorAll('.alert');
        messages.forEach((msg) => {
            setTimeout(() => {
                msg.classList.add('fade-out-custom');

                msg.addEventListener('transitionend', () => {
                    msg.remove();
                });
            }, 3000);
        });
    }
}