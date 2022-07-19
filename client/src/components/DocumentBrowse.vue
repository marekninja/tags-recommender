<template>
    <div>
        <div class="d-flex flex-wrap">
            <span class="badge text-bg-info mx-1" v-for="(tag, id) in document.tags" :key="id">
            #{{ tags[tag].text}}
            </span>
        </div>
        <div>
            {{ document.text }}
        </div>
        
    </div>
</template>

<script>

export default {
  name: 'DocumentBrowse',
  props: ['document', 'tags'],
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
