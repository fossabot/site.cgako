<template>

    <div class="row pb-4 mx-auto w-100">
      <b-breadcrumb :items="crumbs"
      class="pr-3 pl-3 p-0 m-0 justify-content-center align-items-center"></b-breadcrumb>
      <button type="button" title="Обновить данные"
      class="btn btn-sm btn-secondary ml-auto" @click="forceRerender">
        <font-awesome-icon icon="sync-alt" fixed-width />
      </button>
    </div>

</template>

<script>
import { EventBus } from '@/utils';

export default {
  name: 'Breadcumbs',
  data() {
    return {
    };
  },
  methods: {
    forceRerender() {
      EventBus.$emit('forceRerender');
    },
  },
  computed: {
    crumbs() {
      const pathArray = this.$route.path.split('/');
      pathArray.shift();
      const breadcrumbs = pathArray.reduce((breadcrumbArray, path, idx) => {
        breadcrumbArray.push({
          route: path,
          to: breadcrumbArray[idx - 1]
            ? `/${breadcrumbArray[idx - 1].route}/${path}`
            : `/${path}`,
          text: this.$route.matched[idx].meta.breadCrumb || path,
        });
        return breadcrumbArray;
      }, []);
      return breadcrumbs;
    },
  },
};
</script>
