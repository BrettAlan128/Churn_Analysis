#target distributon of the churn (pie and countplot)
def plot_target_dist(df):
    sns.set(style = 'whitegrid')
#     sns.set_context('paper', font_scale = 2)
    fig = plt.figure(figsize = (30, 10))
    plt.subplot(121)
    plt.pie(df.Churn.value_counts(), labels = ['No Churn', 'Churn'], autopct = '%.1f%%', radius = 1, textprops={'fontsize': 20, 'fontweight': 'bold'})
    plt.title('Churn Outcome Pie Chart', fontsize = 30, fontweight = 'bold')
    plt.subplot(122)
    churn_numbr = sns.countplot(df.Churn)
    churn_numbr.set_xlabel('Churn', fontweight = 'bold', fontsize = 20)
    churn_numbr.set_ylabel('Count', fontweight = 'bold', fontsize = 20)
    plt.title('Churn Outcome Distributions', fontsize = 30, fontweight = 'bold')
    plt.tight_layout()
#color = '#39ff14'


def plot_hist(NonChurned):
    hist_ax= 1
    fig = plt.figure(figsize = (60, 40))
    for i in range(30):
        plt.subplot(6,6, hist_ax)
        plt.hist(x = num_cols[i], data = NonChurned, label="NonChurned", color = '#39ff14')
        plt.hist(x = num_cols[i], data = Churned, label="Churned",color= '#0f66e9')
        plt.title(num_cols[i] + ' (' + str(hist_ax - 1) + ')', fontsize = 25, fontweight = 'bold')
        plt.ylabel('Count')
        plt.tight_layout()
        hist_ax = hist_ax + 1


def plot_viol(df):
    plot_num = 1
    fig = plt.figure(figsize = (50, 30))
    for i in range(31):
        plt.subplot(6,6, plot_num)
        sns.violinplot(x = 'Churn', y= num_cols[i], data = df, palette = {'Yes':'#39ff14', 'No' : '#0f66e9'} ,scale = 'count')
        plt.title(num_cols[i] + ' (' + str(plot_num - 1) + ')', fontsize = 25, fontweight = 'bold')
        plt.tight_layout()
        plot_num = plot_num + 1






#Not used
def plot_kde(df, feature):
    plt.figure(figsize = (15, 5))
    plt.title(f"KDE Plot: {feature}", fontsize = 30, fontweight = 'bold')
    ax = sns.kdeplot(df[df.Churn1 == 'No'][feature].dropna(), label = 'No Churn', lw = 2, legend = True)
    plt.legend = True
    ax1 = sns.kdeplot(df[df.Churn1 == 'Yes'][feature].dropna(), label = 'Churn', lw = 2, legend = True)
    if feature == 'MonthsInService':
        plt.xlabel('Months In Service', fontsize = 20, fontweight = 'bold')
    else:
        plt.xlabel('Charge Amount ($)', fontsize = 20, fontweight = 'bold')
    plt.tight_layout()