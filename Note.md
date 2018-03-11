# 通用语法
## Statements
### Group Statements 
**Syntax:**

    group_name ( name ) {
      ... statements ...
    }


### Attributes Statements
- Simple Attributes 
- Complex Attributes

#### Simple Attributes 
**Syntax:**

    attribute_name : attribute_value ;

#### Complex Attributes
**Syntax:**

    attribute_name (parameter1, [parameter2, parameter3 ...] );

### Define Statements
**Syntax:**

    define (attribute_name, group_name, attribute_type ) ;

### include_file 语句
可用于减小文件大小。例如：

    cell() {
      area : 0.1 ;
      ...
      include_file (memory_file) ;
      ...
    }

使用限制：

- 不能循环调用，`include_file`调用的文件中不允许存在`include_file`语句；
- 一个`inlcude_file`命令只能调用一个文件；
- `include_file`命令不能替代`group_value`/`attribute_value`语句；
- `include_file`不能替代边界或跨边界存在；

## Library Groups
    library ( my_library ) {
      ...
    }
### 通用属性
- `technology`
- `delay_model`
- `bus_naming_style`

#### technology attribute
**Syntax:**

    technology (name) ;

#### delay_model attribute
**Syntax:**

    delay_model : value ;

#### bus\_nameing\_style attribute
**Syntax:**

    bus_naming_style : "string";

### Delay and Slew Attributes
- `input_threshold_pct_fall`
- `input_threshold_pct_rise`
- `output_threshold_pct_fall`
- `output_threshold_pct_rise`
- `slew_derate_from_library`
- `slew_lower_threshold_pct_fall`
- `slew_lower_threshold_pct_rise`
- `slew_upper_threshold_pct_fall`
- `slew_upper_threshold_pct_rise`

### Definint Unit
- `time_unit` : 1ps / 10ps / 100ps / 1ns
- `voltage_unit` : 1mV / 10mV / 100mV / 1V
- `current_unit` : 1uA / 10uA / 100uA / 1mA / 10mA / 100mA / 1A
- `pulling_resistance_unit` : 1ohm / 10ohm / 100ohm / 1kohm 
- `capacitive_load_unit` : `capacitive_load_unit (value, unit)` - unit : ff / pf
- `leakage_power_unit` : 1W / 100mW / 10mW / 1mW / 100uW / 10uW / 1uW / 100nW / 10nW / 1nW / 100pW / 10pW / 1pW

# Building Environments
    
