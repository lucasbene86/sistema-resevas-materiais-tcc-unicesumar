// =================================== ORDENAR TABELA HTML =====================================
const asc = true;  // ascendente ou descendente
const index = 2;    // coluna de referencia para se ordenar
const tabela_equipamentos = document.getElementById('tabela');

const arr = Array.from(tabela_equipamentos.querySelectorAll('tbody tr'));
const th_elem = tabela_equipamentos.querySelectorAll('th');

arr.sort((a, b) => {
  const a_val = a.children[index].innerText
  const b_val = b.children[index].innerText
  return (asc) ? a_val.localeCompare(b_val) : b_val.localeCompare(a_val)
})
arr.forEach(elem => {
  tabela_equipamentos.appendChild(elem)
});