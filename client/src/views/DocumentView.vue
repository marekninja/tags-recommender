<template>
  <div class="home container">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      documents: [
        {
          id: 1,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3, 0, 1, 2, 3,0, 1, 2, 3, 0, 1, 2, 3,0, 1, 2, 3, 0, 1, 2, 3,0, 1, 2, 3, 0, 1, 2, 3,]
        },
        {
          id: 2,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
        {
          id: 3,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
        {
          id: 4,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
        {
          id: 5,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
        {
          id: 6,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
        {
          id: 7,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
        {
          id: 8,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
        {
          id: 9,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius lacinia odio id consectetur. Duis sit amet tellus ac libero luctus sollicitudin vel et eros. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Etiam vestibulum risus eu diam maximus, sit amet porttitor urna ultrices. Ut semper fermentum tortor eu fermentum. In sagittis libero malesuada orci vulputate efficitur. Vestibulum eget rutrum massa, et tristique mauris. Praesent urna ante, luctus ut placerat quis, semper et eros. Maecenas pharetra porta augue in faucibus. Nam ultrices cursus facilisis. Nunc pretium vulputate massa sed ultrices. Ut eget lorem non augue tincidunt laoreet. Ut euismod aliquet arcu a scelerisque. Nulla in dignissim magna.",
          tags: [0, 1, 2, 3]
        },
      ],
      tags: [
        {id: 0, text: "exciting"},
        {id: 1, text: "new"},
        {id: 2, text: "important"},
        {id: 3, text: "optional"},
        {id: 4, text: "science"},
      ]
    }
  }
}
</script>
