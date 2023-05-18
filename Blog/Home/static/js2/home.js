const deg = 6;
const hr = document.querySelector('#hr');
const mn = document.querySelector('#mn');
const sc = document.querySelector('#sc');

setInterval(() =>{
    
     let day = new Date();
let hh = day.getHours() * 30;
let mm = day.getMinutes() * deg;
let ss = day.getSeconds() * deg;

hr.style.transform = `rotateZ(${(hh)+(mm/12)}deg)`;
mn.style.transform = `rotateZ(${mm}deg)`;
sc.style.transform = `rotateZ(${ss}deg)`;
    
})

function goBack() {
     window.history.back();
   }
// Lấy tất cả các thẻ a có class "link"
const links = document.querySelectorAll(".link");

// Duyệt qua tất cả các thẻ a và thêm sự kiện click
links.forEach(link => {
  link.addEventListener("click", function() {
    // Xóa class "active" khỏi tất cả các thẻ a
    links.forEach(link => link.classList.remove("active"));

    // Thêm class "active" vào thẻ a được click
    this.classList.add("active");
  });
});
