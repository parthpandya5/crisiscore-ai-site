<template>
  <b-container id="contact" class="py-5 bg-white">
    <h2 class="text-center text-primary mb-4">Get In Touch</h2>
    <b-row class="justify-content-center">
      <b-col cols="12" md="8">
        <b-form @submit.prevent="submitForm">
          <b-form-group label="Your Name" label-for="nameInput">
            <b-form-input id="nameInput" v-model="form.name" required />
          </b-form-group>

          <b-form-group label="Your Email" label-for="emailInput">
            <b-form-input
              id="emailInput"
              type="email"
              v-model="form.email"
              required
            />
          </b-form-group>

          <b-form-group label="Message" label-for="messageInput">
            <b-form-textarea
              id="messageInput"
              v-model="form.message"
              rows="4"
              required
            />
          </b-form-group>

          <div class="text-center">
            <b-button type="submit" variant="primary">Send Message</b-button>
          </div>
        </b-form>
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup>
import { reactive } from 'vue'

const form = reactive({
  name: '',
  email: '',
  message: '',
})

function submitForm() {
  // TODO: hook into an email service or Firebase function
  alert(`Thanks, ${form.name}! We’ve received your message.`)
  form.name = ''
  form.email = ''
  form.message = ''
}
</script>

<style scoped>
#contact {
  scroll-margin-top: 60px;
}
</style>
