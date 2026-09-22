// =========================
// SmartMail AI
// script.js
// =========================


// =========================
// Search Emails
// =========================

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        let value = this.value.toLowerCase();

        let cards = document.querySelectorAll(".email-card");

        cards.forEach(card => {

            let text = card.dataset.search.toLowerCase();

            if (text.includes(value)) {

                card.style.display = "block";

            } else {

                card.style.display = "none";

            }

        });

    });

}



// =========================
// Filter Emails
// =========================

function filterEmails(priority) {

    let cards = document.querySelectorAll(".email-card");

    let buttons = document.querySelectorAll(".filter-btn");

    buttons.forEach(btn => {

        btn.classList.remove("active-filter");

    });

    event.target.classList.add("active-filter");


    cards.forEach(card => {

        if (priority === "All") {

            card.style.display = "block";

        }

        else if (card.dataset.priority === priority) {

            card.style.display = "block";

        }

        else {

            card.style.display = "none";

        }

    });

}



// =========================
// Fade Animation
// =========================

window.onload = function () {

    let cards = document.querySelectorAll(".email-card");

    cards.forEach((card, index) => {

        setTimeout(() => {

            card.classList.add("fade-in");

        }, index * 60);

    });

};



// =========================
// Sync Gmail Button
// (Temporary)
// =========================

const syncButton = document.querySelector(".sync-btn");

if (syncButton) {

    syncButton.addEventListener("click", function () {

        this.innerHTML = '<i class="bi bi-arrow-repeat"></i> Syncing...';

        this.disabled = true;

        setTimeout(() => {

            location.reload();

        }, 1500);

    });

}