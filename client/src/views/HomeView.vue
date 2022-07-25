<template>
  <div class="home container">
    <div class="d-inline-flex">
      <div class="d-flex align-items-center">
        <h1> Ayanza SW &amp; ML Engineer assignment </h1>
      </div>
    </div>

    <DocumentBrowse v-for="doc in documents" :key="doc.id" :document="doc" :tags="tags"/>

  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import DocumentBrowse from '@/components/DocumentBrowse.vue'

export default {
  name: 'HomeView',
  components: {
    // HelloWorld,
    DocumentBrowse
  },
   mounted() {
    this.axios.get("docs")
        .then((response => {
          console.log(response.data);
          this.documents = response.data

          this.axios.get("tags")
            .then((response => {
              console.log(response.data);
              this.tags = response.data
            }))
        }));

  },
  data() {
    return {
      documents: [],
      tags: [],
      // documents: [
      //   {
      //     id: 1,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3, 0, 1, 2, 3,0, 1, 2, 3, 0, 1, 2, 3,0, 1, 2, 3, 0, 1, 2, 3,0, 1, 2, 3, 0, 1, 2, 3,]
      //   },
      //   {
      //     id: 2,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      //   {
      //     id: 3,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      //   {
      //     id: 4,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      //   {
      //     id: 5,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      //   {
      //     id: 6,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      //   {
      //     id: 7,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      //   {
      //     id: 8,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      //   {
      //     id: 9,
      //     text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
      //     tags: [0, 1, 2, 3]
      //   },
      // ],
      // tags: [
      //   {id: 0, text: "exciting"},
      //   {id: 1, text: "new"},
      //   {id: 2, text: "important"},
      //   {id: 3, text: "optional"},
      //   {id: 4, text: "science"},
      // ]
    }
  }
}
</script>
