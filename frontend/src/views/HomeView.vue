<template>
  <div class="home">
    <h1 class="title">TodoApp: Django + Vue</h1>
    <div class="columns mt-6">
      <div class="column is-2 is-offsett-2">
        <h2 class="subtitle">New Task</h2>
        <form v-on:submit.prevent="addTask">
          <div class="field">
            <label class="label has-text-left" for="newTaskTitle">Title</label>
            <div class="control">
              <input v-model="newTaskTitle" id="newTaskTitle" class="input" type="text" name="title" required>
            </div>
          </div>
          <div class="field">
            <label class="label has-text-left" for="newTasksDescription">Description</label>
            <div class="contro">
              <textarea v-model="newTaskDescription" id="newTaskDescription" class="textarea" name="description" cols="30" rows="5"></textarea>
            </div>
          </div>
          <div class="field is-flex is-align-items-flex-end" style="gap: 5px;">
            <label class="label" for="newTaskStatus">Status</label>
            <div class="select">
              <select v-model="newTaskStatus" id="newTaskStatus" name="status" required>
                <option value="P">In Progress</option>
                <option value="D">Done</option>
              </select>
            </div>
          </div>
          <div class="field has-text-right">
            <div class="control">
              <button class="button is-link" type="submit">Save</button>
            </div>
          </div>
        </form>
      </div>
      <div class="column is-5">
        <h2 class="subtitle">In Progress</h2>
        <div class="card" v-for="task in tasks" v-if="task.status === 'P'" v-bind="task.id">
          <div class="card-header mt-3">
            <h3 class="card-header-title">{{ task.title }}</h3>
          </div>
          <div class="card-content">
            <p v-if="task.description !== ''">{{ task.description }}</p>
            <p v-else>You doesn't provide any description for this task</p>
          </div>
          <div class="card-footer">
            <div class="card-footer-item">
              <button class="button is-link" v-on:click="setTaskStatus(task.id, 'D')">Done</button>
            </div>
          </div>
        </div>
      </div>
      <div class="column is-5">
        <h2 class="subtitle">Done</h2>
        <div class="card mt-3" v-for="task in tasks" v-if="task.status === 'D'" v-bind="task.id">
          <div class="card-header">
            <h3 class="card-header-title">{{ task.title }}</h3>
          </div>
          <div class="card-content">
            <p v-if="task.description !== ''">{{ task.description }}</p>
            <p v-else>You doesn't provide any description for this task</p>
          </div>
          <div class="card-footer">
            <div class="card-footer-item">
              <button class="button is-link" v-on:click="setTaskStatus(task.id, 'P')">Repeat</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'HomeView',
  data() {
    return {
      tasks: [],
      newTaskTitle: "",
      newTaskDescription: "",
      newTaskStatus: "P"
    }
  },
  mounted() {
    this.getTasks()
  },
  methods: {
    getTasks() {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/tasks/',
        auth: {
          username: 'admin',
          password: 'password'
        }
      }).then(response => this.tasks = response.data)
    },
    addTask() {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/tasks/',
        auth: {
          username: 'admin',
          password: 'password'
        },
        data: {
          owner: '1',
          title: this.newTaskTitle,
          description: this.newTaskTescription,
          status: this.newTaskStatus
        }
      }).then((response) => {
        this.tasks.push({
          id: response.data.id,
          title: response.data.title,
          description: response.data.description,
          status: response.data.status
        })
        this.newTaskTitle = ""
        this.newTaskDescription = ""
        this.newTaskStatus = "P"
      }).catch((error) => {
        console.log(error)
      })
    },
    setTaskStatus(task_id, status) {
      axios({
        method: 'patch',
        url: `http://127.0.0.1:8000/tasks/${task_id}/`,
        headers: {
          'Content-Type': 'application/json'
        },
        auth: {
          username: 'admin',
          password: 'password'
        },
        data: {
          status: status
        }
      }).then(() => {
        this.tasks.filter(task => task.id === task_id)[0].status = status
      })
    }
  }
}
</script>
