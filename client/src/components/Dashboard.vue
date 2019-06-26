<template>
    <main class="container-fluid">
        <breadcumbs></breadcumbs>

        <b-row class="pb-3">

          <b-col cols="3">
            <b-card no-body class="overflow-hidden shaded"
            style="max-width: 540px;">
              <b-row no-gutters>
                <b-col sm="6" class="text-primary my-auto
                justify-content-center align-middle align-items-center text-center">
                  <font-awesome-icon :icon="['fa', 'user']" fixed-width size="3x"/>
                </b-col>
                <b-col sm="6" class="bg-primary text-white
                justify-content-center align-middle align-items-center text-center">
                  <b-card-body>
                    <b-card-text>
                      <h2 class="">15</h2>
                      <span class="notation">
                        Польз. CMS
                      </span>
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
          <b-col cols="3">
            <b-card no-body class="overflow-hidden shaded"
            style="max-width: 540px;">
              <b-row no-gutters>
                <b-col sm="6" class="text-info my-auto
                justify-content-center align-middle align-items-center text-center">
                  <font-awesome-icon :icon="['fa', 'users']" fixed-width size="2x"/>
                </b-col>
                <b-col sm="6" class="bg-info text-white
                justify-content-center align-middle align-items-center text-center">
                  <b-card-body>
                    <b-card-text>
                      <h2 class="">150</h2>
                      <span class="notation">
                        Клиентов
                      </span>
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
          <b-col cols="3">
            <b-card no-body class="overflow-hidden shaded"
            style="max-width: 540px;">
              <b-row no-gutters>
                <b-col sm="6" class="text-success my-auto
                justify-content-center align-middle align-items-center text-center">
                  <font-awesome-icon :icon="['fa', 'newspaper']" fixed-width size="2x"/>
                </b-col>
                <b-col sm="6" class="bg-success text-white
                justify-content-center align-middle align-items-center text-center">
                  <b-card-body>
                    <b-card-text>
                      <h2 class="">350</h2>
                      <span class="notation">
                        Новостей
                      </span>
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </b-col>
          <b-col cols="3">
            <b-card no-body class="overflow-hidden shaded"
            style="max-width: 540px;">
              <b-row no-gutters>
                <b-col sm="6" class="text-warning my-auto
                justify-content-center align-middle align-items-center text-center">
                  <font-awesome-icon :icon="['fa', 'list']" fixed-width size="2x"/>
                </b-col>
                <b-col sm="6" class="bg-warning text-white
                justify-content-center align-middle align-items-center text-center">
                  <b-card-body>
                    <b-card-text>
                      <h2 class="">5</h2>
                      <span class="notation">
                        Разделов
                      </span>
                    </b-card-text>
                  </b-card-body>
                </b-col>
              </b-row>
            </b-card>
          </b-col>

        </b-row>

        <b-row>
          <b-col cols="8">
            <b-card
              border-variant="secondary"
              header="Траффик сайта"
              header-border-variant="secondary"
              align="center"
            >
              <b-card-text>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</b-card-text>
            </b-card>
          </b-col>
          <b-col cols="4">
            <b-card
              border-variant="secondary"
              header="Места просмотра"
              header-border-variant="secondary"
              align="center"
            >
              <b-card-text>Lorem ipsum dolor sit amet</b-card-text>
            </b-card>
          </b-col>
        </b-row>
    </main>
</template>

<script>
import Breadcumbs from './Breadcumbs';

export default {
  name: 'Dashboard',
  data() {
    return {
    };
  },
  components: { Breadcumbs },
};
</script>
