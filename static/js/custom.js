// let buttons = document.querySelectorAll('button');
// console.log(buttons)
// buttons.forEach(button => {
//     button.addEventListener('click', function() {
//         buttons.forEach(btn => btn.classList.remove('active'));
//         this.classList.add('active');
//     });
// });


document.addEventListener("DOMContentLoaded", function() {
    let btn = document.querySelectorAll(".filter-button")
    console.log(":asdsa", btn)
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            console.log("djfhjksadfhjksdafjkesfh")
                // buttons.forEach(btn => btn.classList.remove('active'));
                // this.classList.add('active');
        });
    });
});
// document.addEventListener("DOMContentLoaded", () => {
//     const items = document.querySelectorAll('.filter-button');

//     items.forEach((item, idx) => {
//         item.addEventListener('click', () => {
//             ToggleActive(item, idx);
//         });
//     });

//     function ToggleActive(el, index) {
//         el.classList.toggle('active');
//         items.forEach((item, idx) => {
//             if (idx !== index) {
//                 item.classList.remove("active");
//             }
//         });
//     }
// })