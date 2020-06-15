<template>
  <div>

    <section class='purposeSection'>

      <div class='titleArea'>
        <h1 class='center blueColor fontSizeHeadings'>Purpose</h1>
      </div>

      <div class='paragraphDiv'>
        <p>
          The title of this project is 3 Speeches. As the title states, the goal
          is to examine three important speeches in U.S. History. This is also
          the third time I've done this project. The goal now is to use some
          sentiment analysis to see if that can tell us more about each of the
          speeches that will be investigated in this project. Also, unlike my
          previous projects, I will not be including the actual speeches in this
          project. Instead, I'll have links to the speech. Other than that I'll
          also work to improve some of my basic HTML/CSS skills to try and make
          the website look nice.
        </p>
      </div>

    </section>

  </div>
</template>

<script>
</script>

<style scoped>

.purposeSection {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 2em;
}

.titleArea {
  display: flex;
  justify-content: center;
  align-items: center;
}

.paragraphDiv p {
  font-size: 20px;
  margin-left: 5%;
  margin-right: 5%;
}

@media only all and (max-width: 900px){

  .purposeSection {
    grid-template-columns: 1fr;
  }

  .paragraphDiv  {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
  }

}

</style>
