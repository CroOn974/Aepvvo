<template>
  <v-sheet width="500" class="mx-auto ma-10">
    <v-form @submit.prevent="submitForm">
      <v-row>
        <v-col cols="6">
          <v-autocomplete v-model="car.manufacturer" label="Manufacturer" :items=this.ManufacturerList></v-autocomplete>
          <v-autocomplete v-model="car.category" label="Category" :items=this.categoryList></v-autocomplete>
          <v-text-field v-model.number="car.mileage" label="Mileage" type="number"></v-text-field>
          <v-autocomplete v-model="car.gearBox" label="Gear Box" :items=this.gearBoxList></v-autocomplete>
          <v-text-field v-model.number="car.engine" label="Engine volume" type="number"></v-text-field>
          <v-autocomplete v-model="car.driveWheels" label="Drive Wheels" :items=this.driveWheelsList></v-autocomplete>
          <v-autocomplete v-model="car.cylinders" label="Cylinders" :items=this.cylindersList></v-autocomplete>
        </v-col>
        <v-col cols="6">
          <v-autocomplete v-model="car.model" label="Model" :items=this.ModelList></v-autocomplete>
          <v-text-field v-model.year="car.year" label="Year" type="number"></v-text-field>
          <v-text-field v-model.year="car.airbag" label="Airbags Number" type="number"></v-text-field>
          <v-text-field v-model.year="car.levy" label="Levy" type="number"></v-text-field>
          <v-select v-model="car.leather" label="Leather interior" :items="['Yes', 'No']"></v-select>
          <v-select v-model="car.turbo" label="Turbo" :items="['Yes', 'No']"></v-select>
          <v-autocomplete v-model="car.fuelType" label="Fuel type" :items=this.fuelList></v-autocomplete>
        </v-col>
      </v-row>
      
      <v-btn type="submit" block class="mt-2">Submit</v-btn>
    </v-form>
  </v-sheet>
</template>

<script>
export default {
  data() {
    return {
      host:'http://localhost:8000/',
      ManufacturerList: [],
      ModelList: [],
      categoryList: [],
      fuelList: [],
      gearBoxList: [],
      driveWheelsList: [],
      cylindersList:[],
      car :{
        manufacturer: null,
        model: null,
        year: null,
        category: null,
        fuelType: null,
        mileage: null,
        gearBox: null,
        engine: null,
        leather: null,
        airbag: null,
        levy: null,
        cylinders: null,
      }

    };
  },
  async created(){
    this.getManufacturer()
    this.getModel()
    this.getCategory()
    this.getFuelType()
    this.getGearBox()
    this.getDriveWheels()
    this.getCylinders()

  },
  watch: {
    'car.manufacturer': function() {
      this.getModel();
    }
  },
  methods: {
    submitForm() {
      const data = this.car
      console.log(data);
      this.getPredic()
    },
    async getManufacturer(){

      var response = await fetch(this.host+'/api/manufacturer/');
      const data = await response.json();

      const manufacturers = [];

      for (let i = 0; i < data.length; i++) {
        manufacturers.push(data[i].manufacturer_libele);
      }

      this.ManufacturerList = manufacturers;
      

    },
    async getModel(){
      
      if(this.car.manufacturer) {
        var response = await fetch(this.host+'/api/model/'+this.car.manufacturer+'');
        const data = await response.json();
        console.log();
        const models = [];

        for (let i = 0; i < data.length; i++) {
          models.push(data[i].model_libele);
        }

        this.ModelList = models;

      }

    },
    async getCategory(){

      var response = await fetch(this.host+'/api/category/');
      const data = await response.json();

      const category = [];

      for (let i = 0; i < data.length; i++) {
        category.push(data[i].category_libele);
      }

      this.categoryList = category;

    },
    async getFuelType(){

      var response = await fetch(this.host+'/api/fuels/');
      const data = await response.json();

      const fuel = [];

      for (let i = 0; i < data.length; i++) {
        fuel.push(data[i].fuel_type);
      }

      this.fuelList = fuel;

    },
    async getGearBox(){
      var response = await fetch(this.host+'/api/gearbox/');
      const data = await response.json();

      const gearBox = [];

      for (let i = 0; i < data.length; i++) {
        gearBox.push(data[i].gearbox_type);
      }

      this.gearBoxList = gearBox;
    },
    async getDriveWheels(){
      var response = await fetch(this.host+'/api/drivewheels/');
      const data = await response.json();

      const driveWheels = [];

      for (let i = 0; i < data.length; i++) {
        driveWheels.push(data[i].drivewheels_type);
      }

      this.driveWheelsList = driveWheels;

    },
    async getCylinders(){
      var response = await fetch(this.host+'/api/cylinders/');
      const data = await response.json();

      const cylinders = [];

      for (let i = 0; i < data.length; i++) {
        cylinders.push(data[i].cylenders_number);
      }

      this.cylindersList = cylinders;
    },
    async getPredic(){
      var response = await fetch(this.host+'/api/predict/',{
          method:'post',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.car)   
      });

      console.log(response);
    }
  }
};
</script>