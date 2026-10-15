// script.js
const trustTabs = document.querySelectorAll(".trust-tab");
const trustMessages = document.querySelectorAll(".trust-message");

trustTabs.forEach((tab) => {
    tab.addEventListener("click", () => {
        const targetId = tab.dataset.target;

        trustTabs.forEach((item) => {
            const isSelected = item === tab;
            item.classList.toggle("is-active", isSelected);
            item.setAttribute("aria-selected", String(isSelected));
        });

        trustMessages.forEach((message) => {
            message.classList.toggle("is-visible", message.id === targetId);
        });
    });
});