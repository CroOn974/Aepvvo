<template>
<router-view/>
<v-container class = "d-flex flex-wrap">

    <v-col align-self="start" lg="5" class="colonnes">

      <v-row class="ligne1" align-content="center" justify="center">
        
          <v-text-field
            align-self="center"
            bg-color="blue"
            v-model="firstName"
            :rules="rules"
            label="Marque"
          >
          </v-text-field>
        
          <v-text-field
            v-model="firstName"
            :rules="rules"
            label="Modèle"
          >
          </v-text-field>

          <v-text-field
            v-model="firstName"
            :rules="rules"
            label="Taille"
          >
          </v-text-field>

          <v-text-field
            align-self="center"
            bg-color="blue"
            v-model="firstName"
            :rules="rules"
            label="First name"
          >
          </v-text-field>

      </v-row>


    <v-row class="ligne2" cols="start">

          <v-text-field
            align-self="center"
            bg-color="blue"
            v-model="firstName"
            :rules="rules"
            label="First name"
          >
          </v-text-field>

        
          <v-text-field
            v-model="firstName"
            :rules="rules"
            label="Valeur"
          >
          </v-text-field>

          <v-text-field
            bg-color="yellow"
            v-model="firstName"
            :rules="rules"
            label="Taille"
          >
          </v-text-field>

          <v-text-field
            align-self="center"
            bg-color="red"
            v-model="firstName"
            :rules="rules"
            label="First name"
          >
          </v-text-field>

      </v-row>

      <v-row class="ligne3" cols="start">

          <v-text-field
            align-self="center"
            bg-color="blue"
            v-model="firstName"
            :rules="rules"
            label="First name"
          >
          </v-text-field>


          <v-text-field
            v-model="firstName"
            :rules="rules"
            label="Valeur"
            >
          </v-text-field>

          <v-text-field
            bg-color="yellow"
            v-model="firstName"
            :rules="rules"
            label="Taille"
          >
          </v-text-field>

          <v-text-field
            align-self="center"
            bg-color="red"
            v-model="firstName"
            :rules="rules"
            label="First name"
          >
          </v-text-field>

          </v-row>

      <v-row class="ligneB" justify="center">
        <v-col class="colBout"  >
          <v-btn class="bouttonF" size="large">Calculer le prix</v-btn>
        </v-col>
      </v-row>

    </v-col>

</v-container>
</template>


<!-- ///////////////////////////// LE SCRIPT ICI////////////////////////////////////// -->
<script>

</script>



<!--////////////////////////////// Ici le CSS //////////////////////////////////////////-->
<style>
.colonnes{

}
.bouttonF { 
  background-color: black;
margin: auto; 
}

.colBout{
  display: flex;
}

.ligne1{
  display: flex;
}

.ligne2 {
  display: flex;
}

.ligne3{
  display: flex;
}
</style>
