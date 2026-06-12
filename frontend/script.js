const API_URL = "http://127.0.0.1:8000/api/usuarios";

const form = document.getElementById("formUsuario");
const tabela = document.getElementById("tabelaUsuarios");

async function carregarUsuarios() {
  const resposta = await fetch(API_URL);
  const usuarios = await resposta.json();

  tabela.innerHTML = "";

  usuarios.forEach(usuario => {
    tabela.innerHTML += `
      <tr>
        <td>${usuario.id}</td>
        <td>${usuario.nome}</td>
        <td>${usuario.email}</td>
        <td>${usuario.telefone}</td>
        <td>
          <button class="editar" onclick="editarUsuario(${usuario.id}, '${usuario.nome}', '${usuario.email}', '${usuario.telefone}')">Editar</button>
          <button class="excluir" onclick="excluirUsuario(${usuario.id})">Excluir</button>
        </td>
      </tr>
    `;
  });
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const id = document.getElementById("id").value;

  const usuario = {
    nome: document.getElementById("nome").value,
    email: document.getElementById("email").value,
    telefone: document.getElementById("telefone").value,
    senha: document.getElementById("senha").value
  };

  if (id) {
    await fetch(`${API_URL}/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(usuario)
    });
  } else {
    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(usuario)
    });
  }

  form.reset();
  document.getElementById("id").value = "";
  carregarUsuarios();
});

function editarUsuario(id, nome, email, telefone) {
  document.getElementById("id").value = id;
  document.getElementById("nome").value = nome;
  document.getElementById("email").value = email;
  document.getElementById("telefone").value = telefone;
}

async function excluirUsuario(id) {
  await fetch(`${API_URL}/${id}`, {
    method: "DELETE"
  });

  carregarUsuarios();
}

carregarUsuarios();