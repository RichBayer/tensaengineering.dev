(() => {
  const terms = Array.from(document.querySelectorAll(".glossary-term[data-definition]"));

  if (!terms.length) {
    return;
  }

  const tooltip = document.createElement("div");
  tooltip.className = "glossary-tooltip";
  tooltip.hidden = true;
  tooltip.setAttribute("role", "dialog");
  tooltip.setAttribute("aria-live", "polite");

  document.body.appendChild(tooltip);

  function hideTooltip() {
    tooltip.hidden = true;
    tooltip.innerHTML = "";
  }

  function positionTooltip(trigger) {
    const rect = trigger.getBoundingClientRect();
    const spacing = 10;

    tooltip.hidden = false;

    const tooltipRect = tooltip.getBoundingClientRect();
    let left = rect.left;
    let top = rect.bottom + spacing;

    if (left + tooltipRect.width > window.innerWidth - 16) {
      left = window.innerWidth - tooltipRect.width - 16;
    }

    if (left < 16) {
      left = 16;
    }

    if (top + tooltipRect.height > window.innerHeight - 16) {
      top = rect.top - tooltipRect.height - spacing;
    }

    if (top < 16) {
      top = 16;
    }

    tooltip.style.left = `${left}px`;
    tooltip.style.top = `${top}px`;
  }

  function showTooltip(trigger) {
    const term = trigger.dataset.term || trigger.textContent.trim();
    const definition = trigger.dataset.definition;
    const href = trigger.getAttribute("href");

    tooltip.innerHTML = `
      <button class="glossary-tooltip-close" type="button" aria-label="Close glossary definition">×</button>
      <strong>${term}</strong>
      <span>${definition}</span>
      <a href="${href}">Read glossary entry</a>
    `;

    tooltip.querySelector(".glossary-tooltip-close").addEventListener("click", hideTooltip);
    positionTooltip(trigger);
  }

  terms.forEach((term) => {
    term.addEventListener("click", (event) => {
      event.preventDefault();
      showTooltip(term);
    });

    term.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        showTooltip(term);
      }
    });
  });

  document.addEventListener("click", (event) => {
    if (
      tooltip.hidden ||
      tooltip.contains(event.target) ||
      event.target.closest(".glossary-term")
    ) {
      return;
    }

    hideTooltip();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      hideTooltip();
    }
  });

  window.addEventListener("resize", hideTooltip);
  window.addEventListener("scroll", hideTooltip, { passive: true });
})();
