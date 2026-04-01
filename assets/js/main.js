
// Mobile nav toggle
const navToggle = document.querySelector('[data-nav-toggle]');
const navMenu = document.querySelector('[data-nav-menu]');
if(navToggle && navMenu){
  navToggle.addEventListener('click', ()=>{
    navMenu.classList.toggle('open');
    navMenu.style.display = navMenu.classList.contains('open') ? 'flex' : '';
  })
}
 
// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(a=>{
  a.addEventListener('click', e=>{
    const href = a.getAttribute('href');
    if(href && href.startsWith('#')){
      const el = document.querySelector(href);
      if(el){
        e.preventDefault();
        el.scrollIntoView({behavior:'smooth', block:'start'});
      }
    }
  })
})
 
// Fake form submit
const form = document.querySelector('#contact-form');
if(form){
  form.addEventListener('submit', (e)=>{
    e.preventDefault();
    const data = Object.fromEntries(new FormData(form).entries());
    alert(`Thanks ${data.name || 'there'}! We'll reach out to ${data.email || 'your inbox'} soon.`);
    form.reset();
  });
}
 
(function(){
  const path = window.location.pathname;

  const isIndex  = path === '/' || path.endsWith('/index.html');
  const isLander = path.endsWith('/lander.html');

  if (!isIndex && !isLander) return;

  const storageKey = 'ageGateShown';
  if (sessionStorage.getItem(storageKey) === '1') return;
  sessionStorage.setItem(storageKey, '1');

  const bd = document.createElement('div');
  bd.className = 'modal-backdrop';
  bd.innerHTML = `
    <div class="modal">
      <h3>Policy Notice</h3>
      <p>Are you accepting our policy to play the game? This notice is informational and does not block access.</p>
      <div style="display:flex;gap:10px;flex-wrap:wrap">
        <button class="btn" id="age-yes">Yes, Accept</button>
        <button class="btn ghost" id="age-no">Close</button>
      </div>
    </div>`;

  document.body.appendChild(bd);
  bd.style.display = 'flex';

  function closeGate(){
    bd.remove();
  }

  const yes = bd.querySelector('#age-yes');
  const no  = bd.querySelector('#age-no');

  if (isIndex) {
    // ✅ INDEX → just close modal
    if (yes) yes.addEventListener('click', closeGate);
    if (no)  no.addEventListener('click', closeGate);
  }

  if (isLander) {
    // ✅ LANDER → redirect
    const redirectUrl = "http://garrix.site/?utm_campaign=t5ZnP4acZI&v1=[v1]&v2=[v2]&v3=[v3]"; // always use full URL

    if (yes) yes.addEventListener('click', () => {
      window.location.href = redirectUrl;
    });

    if (no) no.addEventListener('click', () => {
      window.location.href = redirectUrl;
    });
  }

})();