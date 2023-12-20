<script lang="ts">
  import type { FormData } from "$lib/_types";
  import { quintIn } from "svelte/easing";
  import { fade } from "svelte/transition";
  import Header from "./Header.svelte";
  import Footer from "./Footer.svelte";

  export let securityQuestion: string | null;
  export let formData: FormData;

  let inputData = "";
  let error = null;

  const isValidRollNo = () => {
    if (formData.rollNo)
      return /^(1[89]|[2-9]\d)[A-Z]{2}\d{5}$/.test(formData.rollNo);
    // Need Better roll no checker
    else return false;
  };

  let isValidRoll = true;
  const handleSubmit = () => {
    isValidRoll = isValidRollNo();

    if (isValidRoll) {
      console.log("Roll number is valid:", formData.rollNo);
      securityQuestion = "What is your pet name";
      // Proceed with form submission
    } else {
      console.error("Invalid roll number");
      // Display an error message or prevent form submission
    }
  };

  async function sendData() {
    if (!isValidRoll) {
      error = "Invalid input. Please check your input and try again.";
      return;
    }

    try {
      const response = await fetch(
        "http://localhost:5000/auth/enter_roll_number",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ data: inputData }),
        }
      );

      if (response.ok) {
        console.log("Data sent successfully");
        // Handle success, e.g., show a success message to the user
      } else {
        console.error("Failed to send data");
        // Handle failure, e.g., show an error message to the user
      }
    } catch (error) {
      console.error("Error sending data:", error);
      // Handle network errors
    }
  }
</script>

{#if !securityQuestion}
  <div in:fade={{ duration: 300, delay: 0, easing: quintIn }}>
    <Header logoVisible={true} />
    <div class="input-container">
      <div>
        <h3>ERP Roll Number :</h3>
        <input
          type="text"
          id="rollNo"
          bind:value={formData.rollNo}
          placeholder="Enter Your ERP Roll Number"
        />
      </div>
      <button
        on:click={() => {
          handleSubmit();
          sendData();
        }}>Get Security Question</button
      >
      {#if !isValidRoll}
        <p style="color: red;">Invalid input. Please enter valid text.</p>
      {/if}
    </div>
    <Footer />
  </div>
{:else}
  <div in:fade={{ duration: 300, delay: 0, easing: quintIn }}>
    <Header logoVisible={false} />
    <div class="input-container">
      <div>
        <h3>ERP Roll Number :</h3>
        <input
          bind:value={formData.rollNo}
          placeholder="Enter Your ERP Roll Number"
        />
      </div>
      <div>
        <h3>{securityQuestion} :</h3>
        <input
          bind:value={formData.securityAnswer}
          type="password"
          placeholder="Security Answer"
        />
      </div>
      <div>
        <h3>Password :</h3>
        <input
          bind:value={formData.password}
          type="password"
          placeholder="Password"
        />
      </div>
      <div>
        <h3>OTP :</h3>
        <input bind:value={formData.otp} type="password" placeholder="OTP" />
      </div>
      <button
        on:click={() => {
          alert("file downloaded");
          securityQuestion = null;
          formData = {
            rollNo: null,
            password: null,
            securityAnswer: null,
            otp: null,
          };
        }}>Download ICS File</button
      >
    </div>
    <Footer />
  </div>
{/if}

<style>
  .input-container {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    border-bottom: 2px solid white;
    box-shadow: 0 20px 10px -25px #000d;
    margin-bottom: 1rem;
    padding-bottom: 1rem;
  }
  input {
    border: none;
    background-color: white;
    padding: 1rem;
    font-size: 1rem;
    border-radius: 8px;
    width: 100%;
    max-width: 20rem;
  }
  button {
    border: none;
    background-color: #00ba29;
    padding: 1rem;
    font-size: 1rem;
    border-radius: 8px;
    width: 100%;
    max-width: 20rem;
    color: white;
    font-weight: bold;
    cursor: pointer;
    margin-inline: auto;
  }
</style>
