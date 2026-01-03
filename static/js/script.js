// Scroll Navbar hanya untuk halaman Home
window.addEventListener("DOMContentLoaded", function () {
  const navbar = document.getElementById("navbar");

  if (window.location.pathname === "/") {
    // Khusus halaman home: scroll effect
    window.addEventListener("scroll", function () {
      if (window.scrollY > 50) {
        navbar.classList.add("fixed", "bg-main-color", "shadow-md");
        navbar.classList.remove("absolute", "mt-1");
      } else {
        navbar.classList.remove("fixed", "bg-main-color", "shadow-md");
        navbar.classList.add("absolute", "mt-1");
      }
    });
  } else {
    // Halaman lain: navbar langsung fixed selalu
    navbar.classList.add("fixed", "bg-main-color", "shadow-md");
    navbar.classList.remove("absolute", "mt-1");
  }
});

// Fungsi active pada navbar
document.addEventListener("DOMContentLoaded", function () {
  const navLinks = document.querySelectorAll("#navbar-sticky a.nav-link");
  const currentURL = window.location.href;

  function setActive(link) {
    navLinks.forEach((nav) =>
      nav.classList.remove(
        "text-white",
        "bg-second-color",
        "md:bg-transparent",
        "md:text-second-color"
      )
    );

    link.classList.add(
      "text-white",
      "bg-second-color",
      "md:bg-transparent",
      "md:text-second-color"
    );
  }

  // Tentukan active otomatis berdasarkan URL
  navLinks.forEach((link) => {
    const href = link.getAttribute("href");

    // contoh: "/" | "/#about" | "/assistant"
    if (
      currentURL === link.href || // halaman yang sama
      (href.includes("#") && currentURL.includes(href)) // scroll section
    ) {
      setActive(link);
    }

    // jaga supaya click tetap menjalankan fungsi active (untuk scroll)
    link.addEventListener("click", () => setActive(link));
  });
});

// Fungsi Active Sidebar
document.addEventListener("DOMContentLoaded", function () {
  const sidebarLinks = document.querySelectorAll(".sidebar-link");

  function setActiveLink(targetHash) {
    sidebarLinks.forEach((link) => {
      link.classList.remove("text-second-color", "bg-neutral-tertiary");
      link.classList.add("text-white");
    });

    const activeLink = document.querySelector(
      `.sidebar-link[href="${targetHash}"]`
    );

    if (activeLink) {
      activeLink.classList.remove("text-white");
      activeLink.classList.add("text-second-color", "bg-neutral-tertiary");
    }
  }

  // Saat halaman pertama kali dibuka
  if (window.location.hash) {
    setActiveLink(window.location.hash);
  } else {
    setActiveLink("#profileData"); // default
  }

  // Saat klik menu sidebar
  sidebarLinks.forEach((link) => {
    link.addEventListener("click", function () {
      setActiveLink(this.getAttribute("href"));
    });
  });
});

// Auto submit Checkbox filter
document.querySelectorAll('input[name="role"]').forEach(cb => {
    cb.addEventListener('change', () => {
      const url = new URL(window.location.href)

      // 🔥 HAPUS category dari path
      const pathParts = url.pathname.split('/')
      if (pathParts.length > 2) {
        url.pathname = '/candidate'
      }

      // submit ulang tanpa category
      document.getElementById('filterForm').action = url.pathname
      document.getElementById('filterForm').submit()
    })
  })