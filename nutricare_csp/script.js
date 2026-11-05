// Initialize Lucide Icons
document.addEventListener("DOMContentLoaded", () => {
  if (window.lucide) {
    lucide.createIcons();
  }
});

// Modal Controller
function openModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.remove("hidden");
    document.body.style.overflow = "hidden";
  }
}

function closeModal(modalId) {
  const modal = document.getElementById(modalId);
  if (modal) {
    modal.classList.add("hidden");
    document.body.style.overflow = "";
  }
}

// Full-screen Image Lightbox Preview
function previewImage(src, caption) {
  const lightbox = document.getElementById("imageLightbox");
  const img = document.getElementById("lightboxImg");
  const captionEl = document.getElementById("lightboxCaption");

  if (lightbox && img && captionEl) {
    img.src = src;
    captionEl.textContent = caption || "";
    lightbox.classList.remove("hidden");
    document.body.style.overflow = "hidden";
  }
}

function closeImagePreview() {
  const lightbox = document.getElementById("imageLightbox");
  if (lightbox) {
    lightbox.classList.add("hidden");
    if (!document.querySelector(".modal-backdrop:not(.hidden)")) {
      document.body.style.overflow = "";
    }
  }
}

// Close modals when clicking backdrop
window.addEventListener("click", (e) => {
  if (e.target.classList.contains("modal-backdrop")) {
    e.target.classList.add("hidden");
    document.body.style.overflow = "";
  }
});

// Close modals & lightbox on Escape key
window.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeImagePreview();
    document.querySelectorAll(".modal-backdrop").forEach((m) => {
      m.classList.add("hidden");
    });
    document.body.style.overflow = "";
  }
});

// Subscription Simulation
function handleSubscribe(e) {
  e.preventDefault();
  const toast = document.getElementById("subToast");
  const input = document.getElementById("emailInput");

  if (toast && input) {
    toast.classList.remove("hidden");
    input.value = "";
    setTimeout(() => {
      toast.classList.add("hidden");
    }, 4000);
  }
}
