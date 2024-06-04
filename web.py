import streamlit as st
import functions

todos = functions.get_todos("userdatafiles/todos.txt")

def add_todo():
    todo = st.session_state["new to-do"]
    new_todo = todo + "\n"
    todos.append(new_todo)
    functions.writelines_todos("userdatafiles/todos.txt", todos)


st.title("To-DoWave")
st.subheader("Turn to-dos into dones")
st.write("Increase your productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.writelines_todos("userdatafiles/todos.txt", todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Enter a to-do", placeholder="Type add, show, edit, tick off or exit: ",
              on_change=add_todo, key="new to-do")
