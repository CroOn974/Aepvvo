<template>
  <v-sheet width="500" class="mx-auto ma-10">
    <v-form @submit.prevent="submitForm">
      <v-autocomplete v-model="car.selectedManufacturer" label="Manufacturer" :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-autocomplete>
      <v-autocomplete v-model="car.selectedModel" label="Model" :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-autocomplete>
      <v-text-field v-model.number="car.year" label="Year" type="number"></v-text-field>
      <v-autocomplete v-model="car.selectedCategory" label="Category" :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-autocomplete>
      <v-select v-model="car.selectedOption" label="Select" :items="['Yes', 'No']"></v-select>
      <v-autocomplete v-model="car.selectedFuelType" label="Fuel type" :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-autocomplete>
      <v-text-field v-model.number="car.mileage" label="Mileage" type="number"></v-text-field>
      <v-btn type="submit" block class="mt-2">Submit</v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
export default {
  data() {
    return {
      car :{
        selectedManufacturer: null,
        selectedModel: null,
        year: null,
        selectedCategory: null,
        selectedOption: null,
        selectedFuelType: null,
        mileage: null
      }

    };
  },
  methods: {
    submitForm() {
      const data = this.car
      console.log(data);
    }
  }
};
</script>