<template>
  <div class="shortcut">
    <section>
      <div class="title">Basic Operations</div>
      <div class="content">
        <ul>
          <li><b>ctrl + z</b><span>Undo</span></li>
          <li><b>ctrl + shift + z</b><span>Redo</span></li>
          <li><b>ctrl + L</b><span>Open/close layer panel</span></li>
          <li><b>ctrl + h</b><span>Open/close reference line</span></li>
          <li><b>ctrl + s</b><span>Data backup</span></li>
        </ul>
      </div>
    </section>
    <section>
      <div class="title">Component Operations</div>
      <div class="content">
        <ul>
          <li><b>ctrl + c</b><span>Copy</span></li>
          <li><b>ctrl + v</b><span>Paste</span></li>
          <li><b>ctrl + click</b><span>Select multiple components</span></li>
          <li><b>ctrl + drag</b><span>Fast copy</span></li>
          <li><b>drag + alt</b><span>Turn off calibration lines and automatic adsorption</span></li>
        </ul>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  methods: {}
}
</script>
<style lang="scss" scoped>
section {
  margin-bottom: 20px;
}
.title {
  font-size: 16px;
  margin-bottom: 6px;
  font-weight: bold;
  color: #000;
}
.content {
  font-size: 14px;
  color: $colorText;
  li {
      margin-bottom: 10px;
    b {
        padding-right: 10px;
    }
    span {
    }
  }
}
</style>
