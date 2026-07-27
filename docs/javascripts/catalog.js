function initializeCatalog() {
  const cards = Array.from(document.querySelectorAll(".resource-card"));
  const search = document.querySelector(".catalog-search");
  const filters = Array.from(document.querySelectorAll(".catalog-filter"));
  const resultCount = document.querySelector(".catalog-result-count");
  const empty = document.querySelector(".catalog-empty");

  if (!cards.length || !search || !resultCount || !empty) return;

  const applyFilters = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let visible = 0;

    cards.forEach((card) => {
      const matchesQuery = !query || card.dataset.search.includes(query);
      const matchesFilters = filters.every((filter) => {
        if (!filter.value) return true;
        const actual = card.dataset[filter.dataset.field] || "";
        return filter.dataset.field === "modalities"
          ? actual.split("|").includes(filter.value)
          : actual === filter.value;
      });
      const show = matchesQuery && matchesFilters;
      card.hidden = !show;
      visible += show ? 1 : 0;
    });

    resultCount.textContent = `显示 ${visible} / ${cards.length} 条`;
    empty.hidden = visible !== 0;
  };

  search.addEventListener("input", applyFilters);
  filters.forEach((filter) => filter.addEventListener("change", applyFilters));
}

if (typeof document$ !== "undefined") {
  document$.subscribe(initializeCatalog);
} else {
  document.addEventListener("DOMContentLoaded", initializeCatalog);
}
