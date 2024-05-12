<template>
  <div style="width: 100%; height: 100%">
    <div>
      <div style="width: 100%; box-sizing: border-box">
        <div style="display: flex; flex-wrap: nowrap; align-items: center">
          <template v-for="(item, logoIndex) in visibleImages" :key="`logo-${logoIndex}`">
            <Image :src="item.itemImageSrc" :alt="item.alt" width="100%" />
          </template>
        </div>
      </div>
    </div>
    <div v-if="Images.length > 0">
      <button style="margin-right: 1%" @click="nextPage" :disabled="currentPage === 0">next</button>
      <button @click="previousPage" :disabled="currentPage === totalPages - 1">previous</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { toRefs, computed, ref, watch } from 'vue'

interface Image {
  itemImageSrc: string
  alt: string
}

const props = defineProps({
  Images: {
    type: Array as () => Image[],
    required: true
  }
})

const { Images } = toRefs(props)

const currentPage = ref(0)
const pageSize = 9

const totalPages = computed(() => Math.ceil(Images.value.length / pageSize))

const visibleImages = computed(() => {
  const startIndex = currentPage.value * pageSize
  const endIndex = startIndex + pageSize
  const reversedImages = Images.value.slice().reverse()
  const visibleReversedImages = reversedImages.slice(startIndex, endIndex)
  return visibleReversedImages.reverse()
})

const previousPage = () => {
  if (currentPage.value < totalPages.value - 1) {
    currentPage.value++
  }
}

const nextPage = () => {
  if (currentPage.value > 0) {
    currentPage.value--
  }
}

watch(
  Images,
  () => {
    currentPage.value = 0
  },
  { deep: true }
)
</script>
